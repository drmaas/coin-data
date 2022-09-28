#!/bin/bash

export DATABASE_URL="postgresql://coin:coin@localhost/coindb"
gunicorn server:app

exit $?
