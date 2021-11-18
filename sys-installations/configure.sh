#!/bin/bash
set -vx

# Error codes
# 100 - exit in error code function
# 101 - exit due to command failure


errCodeChk()
{
  errorCode=$1

  if [ $# -ne 1 ]
  then
    echo "syntax: errCodeChk  <errorCode>"
    echo "errCodeChk expects one parameter"
    exit 100
  fi 

  if [ ${errorCode} -ne 0 ]
  then
    echo "The above step/command failed"
    exit 101
  fi
}

pip install memory_profiler
errCodeChk $?
