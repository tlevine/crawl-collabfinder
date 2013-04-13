#!/bin/sh
set -e

dir="downloads/$(date --rfc-3339 seconds)"
mkdir -p "${dir}"

failuresInARow=0
for projectId in $(seq 1 200); do
  file="${dir}/${projectId}.html"

  wget -O "${file}" "http://collabfinder.com/project/${projectId}"

  if grep "We couldn't find the page you requested." "${file}"; then
    failuresInARow=$(($failuresInARow + 1))
  fi

  if test 10 -lt $failuresInARow; then
    echo Stopped after non-project number $projectId
    exit 0
  fi
done
