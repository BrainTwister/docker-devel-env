#!/usr/bin/env python3

"""
BrainTwister/docker-devel-env - Build list of docker images
"""

__author__ = "Bernd Doser"
__email__ = "bernd.doser@braintwister.eu"
__license__ = "MIT"

import argparse
import itertools
import os
import subprocess
import sys
import yaml

IMAGE_VERSION = '0.6'

def make_image_list(yaml_image_list):
    ''' Generate all combinations of modules and add base images '''

    # Change single modules into list
    for e in yaml_image_list:
        for i, m in enumerate(e):
            if not isinstance(m, list): e[i] = [m]

    # Create base images
    for e in yaml_image_list:
        if len(e) > 1: yaml_image_list.append(e[:-1])

    # Sort and remove duplicates
    yaml_image_list.sort()
    yaml_image_list = list(yaml_image_list for yaml_image_list,_ in itertools.groupby(yaml_image_list))

    # Generate all combinations
    image_list = list()
    for e in yaml_image_list:
        image_list.extend(list(itertools.product(*e)))

    return image_list 


def build_images(image_list, args, docker_push):
    ''' Build and push images '''

    build_status = []
    for image in image_list:

        image_name = '-'.join(image)
        image_name_version = image_name + ':' + IMAGE_VERSION
        if args.verbose == 1:
            print(image_name_version.ljust(90), end='', flush=True)
        elif args.verbose > 1:
            print('Build ' + image_name_version)

        image_base_version = '-'.join(image[:-1]) + ':' + IMAGE_VERSION
        module = image[-1:][0] 

        module_name, module_version = module.rsplit('-', 1)
        module_path = module
        if not os.path.isdir(module_path):
            module_path = module_name
        if not os.path.isdir(module_path):
            raise Exception("Wrong module_path")

        cmd = 'docker build'
        if args.pull:
            cmd += ' --pull'
        if args.no_cache:
            cmd += ' --no-cache'
        cmd += ' -t braintwister/' + image_name_version
        cmd += ' --build-arg VERSION=' + module_version
        if len(image) > 1:
            cmd += ' --build-arg BASE_IMAGE=braintwister/' + image_base_version
        cmd += ' .'

        if args.verbose > 1:
            print('Build command: ' + cmd)

        p = subprocess.Popen(cmd, shell=True, cwd=module_path, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

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
            build_status.append(True)
            if args.verbose == 1:
                print(' passed')
            elif args.verbose > 1:
                print('Build ' + image_name_version + ' successful')
        else:
            build_status.append(False)
            if args.verbose == 1:
                print(' failed')
            elif args.verbose > 1:
                print('Build ' + image_name_version + ' failed')
                print(build_log)
            continue

        # Push to DockerHub
        if docker_push == True:
            subprocess.run('docker push braintwister/' + image_name_version,
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

        # Tag latest version
        if args.latest:
            subprocess.run('docker tag braintwister/' + image_name_version + ' braintwister/' + image_name,
                shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            if docker_push == True:
                subprocess.run('docker push braintwister/' + image_name,
                    shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    return build_status

def main():

    parser = argparse.ArgumentParser(description='Build list of docker images.')
    parser.add_argument('-i', '--images', default='images.yml', help='List of docker images to build (default: images.yml)')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Print more output (two levels)')
    parser.add_argument('-u', '--user', help='Username for docker repository')
    parser.add_argument('-p', '--password', help='Password for docker repository')
    parser.add_argument('--no-cache', action="store_true", help='Do not use cache when building the image')
    parser.add_argument('--pull', action="store_true", help='Always attempt to pull a newer version of the image')
    parser.add_argument('--latest', action="store_true", help='Tag the images as latest version')

    args = parser.parse_args()
    image_list = make_image_list(yaml.load(open(args.images, 'r'), Loader=yaml.FullLoader));
    if args.verbose > 1:
        print('List of images to build:')
        for image in image_list:
            print('-'.join(image) + ':' + IMAGE_VERSION)
        print()

    docker_push = bool(args.user) and bool(args.password)

    # Log in to docker registry
    if docker_push == True:
        if args.verbose > 0:
            print('Login DockerHub')
        cmd = 'echo \'' + args.password + '\'' + ' | docker login -u ' + args.user + ' --password-stdin'
        subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    build_status = build_images(image_list, args, docker_push)

    # Print build status
    if args.verbose > 1:
        print('Build status:')
        for image, status in zip(image_list, build_status):
            print('-'.join(image) + ':' + IMAGE_VERSION + ' %s' % status)
        print()
    print(str(build_status.count(True)) + ' of ' + str(len(build_status)) + ' images successfully built.')

    # Log out from docker registry
    if docker_push == True:
        if args.verbose > 0:
            print('Logout DockerHub')
        cmd = 'docker logout'
        subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    if False in build_status:
        sys.exit(1)

if __name__ == "__main__":
    main()

