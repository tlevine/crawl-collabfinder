#!/bin/sh
set -e

# This converges to normality by the central limit theorem
rnorm() {
  echo $((
    $(($RANDOM % 8)) +
    $(($RANDOM % 8)) +
    $(($RANDOM % 8)) +
    $(($RANDOM % 8)) +
    $(($RANDOM % 8)) +
    $(($RANDOM % 8))
  ))
}

dir="downloads/$(date --rfc-3339 seconds)"
mkdir -p "${dir}"

failuresInARow=0
for projectId in $(seq 1 200); do
  file="${dir}/${projectId}.html"

  wget -O "${file}" "http://collabfinder.com/project/${projectId}" || failuresInARow=$(($failuresInARow + 1))
  sleep $(rnorm)s

  if test 10 -lt $failuresInARow; then
    echo Stopped after non-project number $projectId
    exit 0
  fi
done
