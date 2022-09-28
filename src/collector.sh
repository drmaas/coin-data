#!/bin/bash

export DATABASE_URL="postgresql://coin:coin@localhost/coindb"
python collector.py

exit $?
