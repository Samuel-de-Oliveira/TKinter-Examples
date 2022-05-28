#!/usr/bin/env bash

# If the command don't exist will show a #
# meassage, and exit.                    #
if [ ! -f /usr/bin/$1 ]; then
	echo "This command doesn't exist!"
	exit 1
fi

exec $* # Execute the command in entry.
