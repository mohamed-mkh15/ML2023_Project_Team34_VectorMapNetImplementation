#!/bin/bash

cd "$(dirname "$0")"
cd ..
export PRODUCTION_PATH=$PWD
export ARCH=`uname -m`
export NUM_THREADS=`nproc`

POST_BUILD_SLEEP=10000 \
docker-compose --env-file $PRODUCTION_PATH/build.env \
    -f $PRODUCTION_PATH/build.yml \
    up --build $@
