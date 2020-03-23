#!/bin/sh
./stop
find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete
rm -r temp/
rm common/runtest_args.pckl
