#!/bin/sh

find . -type f -name "*.py[co]" -delete -or -type d -name "__pycache__" -delete
