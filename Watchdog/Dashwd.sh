#!/bin/bash
#make-run.sh
#make sure a process is always running.

#export DISPLAY=:0 #needed if you are running a simple gui app.

process=/home/root/dash.js
makerun="/usr/bin/node  /home/root/dash.js"

if ps | grep -v grep | grep $process > /dev/null
then
    exit
else
    $makerun &
fi

exit
