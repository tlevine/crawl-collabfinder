#!/bin/sh
set -e

# This converges to normality by the central limit theorem
rnorm() {
  echo $((
    $(($RANDOM % 6)) +
    $(($RANDOM % 6)) +
    $(($RANDOM % 6)) +
    $(($RANDOM % 6)) +
    $(($RANDOM % 6)) +
    $(($RANDOM % 6))
  ))
}

dir="projects/$(date --rfc-3339 date)"
mkdir -p "${dir}"
nTries=20

failuresInARow=0
for projectId in $(seq 1 1000); do
  file="${dir}/${projectId}.html"

  test -f "${file}" && continue

  wget -O "${file}" "http://collabfinder.com/project/${projectId}" || failuresInARow=$(($failuresInARow + 1))
  sleep $(rnorm)s

  if test $nTries -lt $failuresInARow; then
    echo Stopped after non-project number $projectId
    exit 0
  fi
done
