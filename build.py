#!/usr/bin/python3

import argparse
import subprocess
import sys
import yaml

def build_images(image_type, image_list, args, docker_push):

    failed = False
    if image_type in image_list:
        for image in image_list[image_type]:

            image_name = '-'.join(image)
            if args.verbose == 1:
                print(image_name.ljust(90), end='', flush=True)
            elif args.verbose > 1:
                print('Build ' + image_name)

            base   = '-'.join(image[:-1])
            module = image[-1:][0] 

            cmd = 'docker build'
            if args.no_cache:
                cmd += ' --no-cache'
            cmd += ' -t braintwister/' + image_name
            if image_type == 'images':
                cmd += ' --build-arg BASE_IMAGE=braintwister/' + base
            cmd += ' .'

            if args.verbose > 1:
                print('Build command: ' + cmd)

            p = subprocess.Popen(cmd, shell=True, cwd=module, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

            if args.verbose > 1:
                print(p.communicate()[0].decode('ascii', errors='ignore'))

            p.wait()
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
                    print(p.communicate()[0].decode('ascii', errors='ignore'))
                failed = True
    return failed

def main():

    parser = argparse.ArgumentParser(description='Build list of docker images.')
    parser.add_argument('-i', '--images', default='images.yml', help='List of docker images to build (default: images.yml)')
    parser.add_argument('-v', '--verbose', action='count', default=0, help='Print more output (two levels)')
    parser.add_argument('-u', '--user', help='Username for docker repository')
    parser.add_argument('-p', '--password', help='Password for docker repository')
    parser.add_argument('--no-cache', action="store_true", help='Do not use cache when building the image')

    args = parser.parse_args()
    image_list = yaml.load(open(args.images, 'r'));

    docker_push = bool(args.user) and bool(args.password)

    # Log in to docker registry
    if docker_push == True:
        if args.verbose > 0:
            print('Login DockerHub')
        cmd = 'echo \'' + args.password + '\'' + ' | docker login -u ' + args.user + ' --password-stdin'
        subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)

    failed = False
    failed |= build_images('base-images', image_list=image_list, args=args, docker_push=docker_push)
    failed |= build_images('images', image_list=image_list, args=args, docker_push=docker_push)

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

