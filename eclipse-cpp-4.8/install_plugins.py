#!/usr/bin/python3

import subprocess
import yaml

stream = open('plugins.yml', 'r')
plugins = yaml.load(stream)

# Uninstall plugins
cmd = '$INSTALLATION_DIR/eclipse/eclipse -noSplash -clean -purgeHistory' \
    + ' -application org.eclipse.equinox.p2.director -destination $INSTALLATION_DIR/eclipse' \
    + ' -uninstallIU '  + ','.join(plugins['uninstall']) \

subprocess.run(cmd, shell=True, check=True)

# Install plugins
for plugin_name, feature_group in plugins['install'].items():
  print('Install ', plugin_name)
  for features in feature_group:
    cmd = '$INSTALLATION_DIR/eclipse/eclipse -noSplash -clean -purgeHistory' \
        + ' -application org.eclipse.equinox.p2.director -destination $INSTALLATION_DIR/eclipse' \
        + ' -repository ' + features['repo'] \
        + ' -installIU '  + ','.join(features['units'])
  
    subprocess.run(cmd, shell=True, check=True)
