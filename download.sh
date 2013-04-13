#!/bin/sh

dir="downloads/$(date --rfc-3339 seconds)"
mkdir -p "${dir}"

failuresInARow=0
for projectId in $(seq 1 200); do
  wget -O "${dir}/${projectId}.html" "http://collabfinder.com/project/${projectId}"
done
