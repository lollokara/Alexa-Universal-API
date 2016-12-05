#!/bin/bash
#make-run.sh
#make sure a process is always running.
#proto ps | grep -v grep | grep /home/root/amazon-echo-bridge-0.4.0.jar 
#export DISPLAY=:0 #needed if you are running a simple gui app.

process=/usr/bin/java
makerun="/usr/bin/java -jar /home/root/amazon-echo-bridge-0.4.0.jar > /dev/null"

if ps | grep -v grep | grep $process > /dev/null
then
    #sudo wall -n not crashed
    exit
else
    $makerun &
    #sudo wall -n running
fi

exit
