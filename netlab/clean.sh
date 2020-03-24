#!/bin/sh

# cleaning script 
# if there is running device inside the root folder
if [ -L "config" ];
then ./stop
fi

# this part is automatic
# under no circumstances leave the pycaches
find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete

if [ -d "temp" ]; then
    rm -r temp/
    rm common/runtest_args.pckl
fi
