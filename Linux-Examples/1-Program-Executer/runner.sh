#!/usr/bin/env bash

if [ ! -f /usr/bin/$1 ]; then
	echo "This command does not exist!"
	exit 1
fi
exec $*
