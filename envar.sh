#!/bin/bash
export FLASK_APP=main.py
export FLASK_APP_SETTINGS="$(pwd)/devel-config"
if [ "$1" = "dev" ];then
  export FLASK_DEBUG=1
  export FLASK_ENV=development
else
  export FLASK_DEBUG=0
  export FLASK_ENV=production
fi