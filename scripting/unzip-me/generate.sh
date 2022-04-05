#!/bin/bash

FLAG_FILE="flag.txt"
NUM=100
FILE="archive-1"

zip $FILE.zip $FLAG_FILE || exit 1

for ((i=2; i <= $NUM; i++)); do
  NEWFILE="archive-$i"
  zip $NEWFILE.zip $FILE.zip
  rm $FILE.zip
  FILE=$NEWFILE
done
