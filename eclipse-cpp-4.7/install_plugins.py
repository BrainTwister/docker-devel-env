#!/usr/bin/python3

import subprocess
import yaml

stream = open('plugins.yml', 'r')
plugins = yaml.load(stream)

for plugin_name, feature_group in plugins.items():
  print(plugin_name)
  for features in feature_group:
    cmd = '$INSTALLATION_DIR/eclipse/eclipse -noSplash -clean -purgeHistory -application org.eclipse.equinox.p2.director -destination $INSTALLATION_DIR/eclipse -repository ' \
        + features['repo'] \
        + ' -installIU' \
        + ' ' + ','.join(features['units']) \
        + ' -tag docker_initial'
  
    subprocess.run(cmd, shell=True, check=True)
