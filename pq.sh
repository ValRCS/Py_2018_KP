#!/usr/bin/env sh

# Get the full path to this script. Will return the right path even if the
# script is symlinked
OLD_PWD="$PWD"
ROOT_DIR="$(dirname "$(readlink -f "$0")")"
VENV_DIR=".venv"
PROJECT_MODULE="pq"

cd "$ROOT_DIR" || exit 1
if [ ! -d "$VENV_DIR" ]; then
    # If the VENV_DIR doesn't exist, the user must have forgotten to run the
    # INSTALL script
    make install
fi
. "$VENV_DIR"/bin/activate

python3 $PROJECT_MODULE "$@"

# Clean up
deactivate
cd "$OLD_PWD" || exit 1
