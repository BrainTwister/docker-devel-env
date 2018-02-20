#!/usr/bin/python3

import argparse
import subprocess
import yaml

parser = argparse.ArgumentParser(description='Build list of docker images.')
parser.add_argument('-i, --images', dest='images', default='images.yml',
    help='List of docker images to build (default: images.yml)')

args = parser.parse_args()
yaml = yaml.load(open(args.images, 'r'));

# Build base images
if 'base-images' in yaml:
    for base_image in yaml['base-images']:
    
        image_name = '-'.join(base_image)
        print(image_name.ljust(90), end='', flush=True)
    
        cmd = 'docker build -t braintwister/' + image_name + ' .'
        log = open(image_name + '.log', "w")
        p = subprocess.run(cmd, shell=True, cwd=image_name, stdout=log, stderr=subprocess.STDOUT)
    
        if p.returncode == 0:
            print(' ... passed')
        else:
            print(' ... failed')

# Build images
if 'images' in yaml:
    for image in yaml['images']:
    
        image_name = '-'.join(image)
        print(image_name.ljust(90), end='', flush=True)
    
        base       = '-'.join(image[:-1])
        module     = image[-1:][0] 
    
        cmd = 'docker build -t braintwister/' + image_name + ' --build-arg BASE_IMAGE=braintwister/' + base + ' .'
        log = open(image_name + '.log', "w")
        p = subprocess.run(cmd, shell=True, cwd=module, stdout=log, stderr=subprocess.STDOUT)
    
        if p.returncode == 0:
            print(' ... passed')
        else:
            print(' ... failed')
