#!/bin/bash
#make-run.sh
#make sure a process is always running.
 
#export DISPLAY=:0 #needed if you are running a simple gui app.

process=server.py
makerun="/usr/bin/python /home/root/server.py"

if ps | grep -v grep | grep $process > /dev/null
then
    exit
else
    $makerun &
fi

exit
