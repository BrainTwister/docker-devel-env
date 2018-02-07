#!/usr/bin/python3

import subprocess
import yaml

stream = open('images.yml', 'r')
yaml = yaml.load(stream)

# Build base images
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
