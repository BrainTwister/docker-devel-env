#!/usr/bin/python3

import argparse
import subprocess
import yaml

parser = argparse.ArgumentParser(description='Install eclipse plugins.')
parser.add_argument('-p, --plugins', dest='plugins', default='plugins.yml',
    help='List of plugins to install (default: plugins.yml)')

args = parser.parse_args()
plugins = yaml.load(open(args.plugins, 'r')) or {};

# Uninstall plugins
if 'unistall' in plugins:
  cmd = '$INSTALLATION_DIR/eclipse/eclipse -noSplash -clean -purgeHistory' \
      + ' -application org.eclipse.equinox.p2.director -destination $INSTALLATION_DIR/eclipse' \
      + ' -uninstallIU '  + ','.join(plugins['uninstall']) \

  subprocess.run(cmd, shell=True, check=True)

# Install plugins
if 'install' in plugins:
  for plugin_name, feature_group in plugins['install'].items():
    print('Install ', plugin_name)
    for features in feature_group:
      cmd = '$INSTALLATION_DIR/eclipse/eclipse -noSplash -clean -purgeHistory' \
          + ' -application org.eclipse.equinox.p2.director -destination $INSTALLATION_DIR/eclipse' \
          + ' -repository ' + ','.join(plugins['general_repos']) + ',' + ','.join(features['repos']) \
          + ' -installIU '  + ','.join(features['units']) \
          + ' -vmargs -Dorg.eclipse.equinox.p2.transport.ecf.retry=5 -Dorg.eclipse.ecf.provider.filetransfer.retrieve.readTimeout=10000'
    
      subprocess.run(cmd, shell=True, check=True)
