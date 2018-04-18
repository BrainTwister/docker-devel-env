#!/bin/bash

# Add conan repositories of conan base module for eclipse user
if [ -f /config/conan_add_repositories.sh ]
then
  /config/conan_add_repositories.sh
fi

echo "USER_ID : $USER_ID"

# Add local user
if [ -n ${USER_ID} ]
then
  GROUP_ID=${GROUP_ID:-${USER_ID}}
  USER_NAME=${USER_NAME:-user}
  GROUP_NAME=${GROUP_NAME:-user}

  echo "USER_ID : $USER_ID"
  echo "GROUP_ID : $GROUP_ID"
  echo "USER_NAME : $USER_NAME"
  echo "GROUP_NAME : $GROUP_NAME"

  groupadd -g $GROUP_ID $GROUP_NAME
  useradd -s /bin/bash -g $GROUP_ID -u $USER_ID -o -c "container user" -m $USER_NAME
  export HOME=/home/$USER_NAME

  exec /usr/local/bin/gosu $USER_NAME "$@"
else
  $@
fi

