#!/bin/sh
#make this script executable: 'chmod +x run.sh'
#must have python installed, and added to your PATH so that the 'python' command works

#if the script is exited prematurely, make sure to shut down authServer
control_c() {
    kill $PID
    exit
}

python authServer.py &
PID=$!
python songAdder.py
kill $PID