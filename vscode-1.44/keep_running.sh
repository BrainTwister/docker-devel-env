#!/bin/bash

# Keep container running until detatched vscode processes are terminated
for i in $(pidof code)
do
  while [ -e /proc/$i ]
    do sleep 0.1
  done
done
