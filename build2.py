#!/usr/bin/python3

import argparse
from enum import Enum
import subprocess
import sys
import yaml

class image_type(Enum):
    base_images = 0
    images = 1

def build_image(image_type):

    if image_type.name in yaml:
        for base_image in yaml[image_type.name]:
        
            image_name = '-'.join(image)
            print(image_name.ljust(90), end='', flush=True)
          
            base       = '-'.join(image[:-1])
            module     = image[-1:][0] 

            if image_type == base_images.base_images:
                cmd = 'docker build -t braintwister/' + image_name + ' .'
                #p = subprocess.run(cmd, shell=True, cwd=image_name, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            else if image_type == base_images.images:
                cmd = 'docker build -t braintwister/' + image_name + ' --build-arg BASE_IMAGE=braintwister/' + base + ' .'
                #p = subprocess.run(cmd, shell=True, cwd=module, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
            
            p = subprocess.run(cmd, shell=True, cwd=module)
          
            if p.returncode == 0:
                print(' ... build passed', end='', flush=True)
                if docker_push == True:
                    cmd = 'docker push braintwister/' + image_name
                    #p2 = subprocess.run(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
                    p2 = subprocess.run(cmd, shell=True)
                    if p2.returncode == 0:
                        print(' ... push passed')
                    else:
                        print(' ... push failed')
                else:
                    print()
                return False
            else:
                print(' ... failed')
                #print(p.stdout.decode('utf-8', errors='ignore'))
                return True
  
def main():

    parser = argparse.ArgumentParser(description='Build list of docker images.')
    parser.add_argument('-i, --images', dest='images', default='images.yml', help='List of docker images to build (default: images.yml)')
    parser.add_argument('-v, --verbose', dest='verbose', default=False, action='store_true', help='Print more output')
    parser.add_argument('-u, --user', dest='user', help='Username for docker repository')
    parser.add_argument('-p, --password', dest='password', help='Password for docker repository')
    
    args = parser.parse_args()
    yaml = yaml.load(open(args.images, 'r'));
    
    failed = False
    docker_push = bool(args.user) and bool(args.password)
    
    print(args.password)
    
    # Log in to docker repository
    if docker_push == True:
        cmd = 'echo \'' + args.password + '\'' + ' | docker login -u ' + args.user + ' --password-stdin'
        subprocess.run(cmd, shell=True)
    
    failed |= build_image(image_type.base-images)
    failed |= build_image(image_type.images)

    # Log out from docker repository
    if docker_push == True:
        cmd = 'docker logout'
        subprocess.run(cmd, shell=True)
    
    if failed == True:
        sys.exit(1)

if __name__ == "__main__":
    main()
