#!/bin/bash

DOCKER_IMAGE='aoc2021:latest'
LABEL_PREFIX='com.adventofcode.coreone'
TRACK_FILES=( Dockerfile poetry.lock pyproject.toml )
SUDO=

SCRIPT_DIR="$( cd -P "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"

if which sha256sum >/dev/null; then
    CHKSUM='sha256sum'
elif which shasum >/dev/null; then
    CHKSUM='shasum -a 256'
elif which md5sum >/dev/null; then
    CHKSUM='md5sum'
else
    echo 'Could not find a checksumming program. Exiting!'
    exit 1
fi


function build() {
    if [ -z "$1" ]; then
        echo 'Image name not provided to build. Exiting!'
        exit 1
    fi
    DOCKER_IMAGE=$1

    if [[ $(git diff --stat) != '' ]]; then
        echo 'Branch is dirty.  The build can only happen on an unmodified branch.'
        exit 2
    fi

    LABELS=
    for tfile in "${TRACK_FILES[@]}"; do
        label="$( $CHKSUM "$tfile" | awk -v PREFIX="$LABEL_PREFIX" '{print PREFIX"."$2"="$1}' )"
        LABELS+="--label ${label} "
    done

    $SUDO docker build --pull -t "$DOCKER_IMAGE" $LABELS .
}


if [ "$TERM" != 'dumb' ] ; then
    TTY='-it'
fi

if [ "$( uname -s )" != 'Darwin' ]; then
    if [ ! -w "$DOCKER_SOCKET" ]; then
        SUDO='sudo'
    fi
fi

pushd "$SCRIPT_DIR" >/dev/null || exit 1

if ! $SUDO docker image ls | awk '{print $1":"$2}' | grep -q "^$DOCKER_IMAGE"; then
    build "$DOCKER_IMAGE"
else
    rebuild='0'
    for tfile in "${TRACK_FILES[@]}"; do
        current="$( $CHKSUM "$tfile" | cut -d' ' -f1 )"
        stored="$( docker image inspect --format="{{index .Config.Labels \"${LABEL_PREFIX}.${tfile}\"}}" "$DOCKER_IMAGE" )"

        if [ "$current" != "$stored" ]; then
            echo "$tfile changed.  Rebuilding."
            rebuild='1'
        fi
    done

    if [ "$rebuild" == "1" ]; then
        echo build "$DOCKER_IMAGE" 2
    fi
fi

$SUDO docker run $TTY --rm -v "$SCRIPT_DIR":/working "$DOCKER_IMAGE" "$@"

popd >/dev/null || exit 1
