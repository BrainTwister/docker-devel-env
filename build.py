#!/usr/bin/env python3

"""
BrainTwister/docker-devel-env - Build list of docker images
"""

__author__ = "Bernd Doser"
__email__ = "bernd.doser@braintwister.eu"
__license__ = "MIT"

import argparse
import itertools
import subprocess
import sys
import yaml

IMAGE_VERSION = '0.1'

def make_image_list(yaml_image_list):
    ''' Generate all combinations of modules '''

    # Change single modules into list
    for e in yaml_image_list:
        for i, m in enumerate(e):
            if not isinstance(m, list): e[i] = [m]

    # Create base images
    for e in yaml_image_list:
        if len(e) > 1: yaml_image_list.append(e[:-1])

    print("1:")
    for e in yaml_image_list:
        print(e)

    # Sort and remove duplicates
    yaml_image_list.sort()
    yaml_image_list = list(yaml_image_list for yaml_image_list,_ in itertools.groupby(yaml_image_list))

    print("2:")
    for e in yaml_image_list:
        print(e)

    image_list = list()
    for e in yaml_image_list:
        image_list.extend(list(itertools.product(*e)))

    return image_list 


def build_images(image_list, args, docker_push):

    failed = False
    for image in image_list:

        image_name = '-'.join(image) + ':' + IMAGE_VERSION
        if args.verbose == 1:
            print(image_name.ljust(90), end='', flush=True)
        elif args.verbose > 1:
            print('Build ' + image_name)

        base   = '-'.join(image[:-1])
        module = image[-1:][0] 

        cmd = 'docker build'
        if args.pull:
            cmd += ' --pull'
        if args.no_cache:
            cmd += ' --no-cache'
        cmd += ' -t braintwister/' + image_name
        if base != '':
            cmd += ' --build-arg BASE_IMAGE=braintwister/' + base
        cmd += ' .'

        if args.verbose > 1:
            print('Build command: ' + cmd)

        p = subprocess.Popen(cmd, shell=True, cwd=module, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        build_log = ''
        while p.poll() is None:
            line = p.stdout.readline().decode('ascii', 'backslashreplace')
            if args.verbose > 1:
                print(line, end='')
            else:
                build_log += line
        line = p.stdout.readline().decode('ascii', 'backslashreplace')
        if args.verbose > 1:
            print(line, end='')
        else:
            build_log += line

        if p.returncode == 0:
            if args.verbose == 1:
                print(' passed')
            elif args.verbose > 1:
                print('Build successful')

            if docker_push == True:

                cmd = 'docker push braintwister/' + image_name

                if args.verbose > 1:
                    print('Push command: ' + cmd)

                p2 = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

                if p2.returncode == 0:
                    print('Push sucessful')
                else:
                    print('Push failed')
                    failed = True
        else:
            print('Build failed')
            if args.verbose <= 1:
                print(build_log)
            failed = True
    return failed

def main():

    parser = argparse.ArgumentParser(description='Build list of docker images.')
    parser.add_argument('-i', '--images', default='images.yml', help='List of docker images to build (default: images.yml)')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Print more output (two levels)')
    parser.add_argument('-u', '--user', help='Username for docker repository')
    parser.add_argument('-p', '--password', help='Password for docker repository')
    parser.add_argument('--no-cache', action="store_true", help='Do not use cache when building the image')
    parser.add_argument('--pull', action="store_true", help='Always attempt to pull a newer version of the image')

    args = parser.parse_args()
    image_list = make_image_list(yaml.load(open(args.images, 'r')));
    print(image_list)

    docker_push = bool(args.user) and bool(args.password)

    # Log in to docker registry
    if docker_push == True:
        if args.verbose > 0:
            print('Login DockerHub')
        cmd = 'echo \'' + args.password + '\'' + ' | docker login -u ' + args.user + ' --password-stdin'
        subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    failed = build_images(image_list, args, docker_push)

    # Log out from docker registry
    if docker_push == True:
        if args.verbose > 0:
            print('Logout DockerHub')
        cmd = 'docker logout'
        subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if failed == True:
        sys.exit(1)

if __name__ == "__main__":
    main()

