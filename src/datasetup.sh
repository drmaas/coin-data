#!/bin/bash

export PYTHONPATH=`pwd`

#export DATABASE_URL="postgres://rqegnmxlbwofhs:VFfK6GeNUaS6UBxnPdA4pRJdrO@ec2-54-221-206-165.compute-1.amazonaws.com:5432/d4ktd1ircmbibs"
export DATABASE_URL="postgresql://coin:coin@localhost/coindb"
python db/datasetup.py

exit $?
