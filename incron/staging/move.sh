#!/bin/bash
/usr/bin/logger "move.sh: FROM $1/$2 TO $3/$2"
mv $1/$2 $3/$2
