#!/bin/bash
commit=$(git log -1 --pretty=%B | head -n 1)
if [[ $commit = *"Release"* ]];
then
  python3 pypi.py
fi
