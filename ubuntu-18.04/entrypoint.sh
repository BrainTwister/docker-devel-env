#!/bin/bash

if [ "$EUID" == "0" ] && [ "$USER_ID" != "0" ]
then 
  # Add local user
  USER_ID=${USER_ID:-9001}
  GROUP_ID=${GROUP_ID:-${USER_ID}}
  USER_NAME=${USER_NAME:-user}
  GROUP_NAME=${GROUP_NAME:-${USER_NAME}}

  groupadd -g $GROUP_ID $GROUP_NAME
  useradd -s /bin/bash -g $GROUP_ID -u $USER_ID -o -c "container user" -m $USER_NAME
  chown -R $USER_NAME:$GROUP_NAME /home/$USER_NAME

  export HOME=/home/$USER_NAME
  cd $HOME

  # Set python local user path
  export PATH=$PATH:/home/$USER_NAME/.local/bin

  # Execute entrypoint modules
  if [ -d "/entrypoint.d" ]; then
    for f in /entrypoint.d/*.sh; do
      . "$f" || break
    done
  fi

  # Execute cmd as user
  chroot --userspec=$USER_NAME --skip-chdir / "$@"
else
  # Execute cmd as root
  $@
fi

# Execute postprocess modules
if [ -d "/postprocess.d" ]; then
  for f in /postprocess.d/*.sh; do
    . "$f" || break
  done
fi
