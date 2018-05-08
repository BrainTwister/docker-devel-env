#!/bin/bash

if [ "$EUID" == "0" ] && [ "$USER_ID" != "0" ]
then 
  # Add local user
  USER_ID=${USER_ID:-9001}
  GROUP_ID=${GROUP_ID:-${USER_ID}}
  USER_NAME=${USER_NAME:-user}
  GROUP_NAME=${GROUP_NAME:-user}

  echo "USER_ID : $USER_ID"
  echo "GROUP_ID : $GROUP_ID"
  echo "USER_NAME : $USER_NAME"
  echo "GROUP_NAME : $GROUP_NAME"

  groupadd -g $GROUP_ID $GROUP_NAME
  useradd -s /bin/bash -g $GROUP_ID -u $USER_ID -o -c "container user" -m $USER_NAME
  chown $USER_NAME:$GROUP_NAME /home/$USER_NAME

  export HOME=/home/$USER_NAME
  cd $HOME

  # Add conan repositories of conan base module for eclipse user
  if [ -f /config/conan_add_repositories.sh ]
  then
    /usr/local/bin/gosu $USER_NAME /config/conan_add_repositories.sh
  fi

  # Add user to docker group and start service
  if grep -qF 'docker' /etc/group
  then 
    usermod -aG docker $USER_NAME
    service docker start
  fi

  exec /usr/local/bin/gosu $USER_NAME "$@"
else
  $@
fi
