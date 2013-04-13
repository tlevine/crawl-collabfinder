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

dir="projects/$(date --rfc-3339 date)"
nTries=10

if test -d "${dir}"; then
  startingPage=$(($nTries + $(ls "${dir}"|sort -n|tail -n1|cut -d. -f1)))
else
  mkdir -p "${dir}"
  startingPage=1
fi

failuresInARow=0
for projectId in $(seq "${startingPage}" 200); do
  file="${dir}/${projectId}.html"

  wget -O "${file}" "http://collabfinder.com/project/${projectId}" || failuresInARow=$(($failuresInARow + 1))
  sleep $(rnorm)s

  if test $nTries -lt $failuresInARow; then
    echo Stopped after non-project number $projectId
    exit 0
  fi
done
