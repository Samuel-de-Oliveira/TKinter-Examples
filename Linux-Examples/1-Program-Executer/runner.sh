#!/usr/bin/env bash

if [ ! -f /usr/bin/$1 ]; then
	exec $* # Execute the command in entry.
fi
