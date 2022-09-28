#!/bin/bash

export PYTHONPATH=`pwd`

export DATABASE_URL="postgresql://coin:coin@localhost/coindb"
python db/datasetup.py

exit $?
