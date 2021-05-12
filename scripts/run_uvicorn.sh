#!/usr/bin/env bash
if [ -z "$HOME_DIR" ]
then
    export HOME_DIR=$(cd "$(dirname $(readlink ${BASH_SOURCE[0]} || echo ${BASH_SOURCE[0]}))/../.." && pwd)
fi

export PYTHONPATH=${HOME_DIR}

python run.py