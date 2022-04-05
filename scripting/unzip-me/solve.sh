#!/bin/bash

NUM=100
FILENAME="archive"

# extract from archive NUM times
for (( i=$NUM; i > 0; i-- )); do
  FILE="$FILENAME-$i.zip"
  unzip $FILE
  rm $FILE
done
