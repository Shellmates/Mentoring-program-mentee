#!/bin/bash

FLAG_FILE="flag.txt"
NUM=100
FILE="archive-revenge-1"
PASS_FILE="password.txt"

password() {
  head -c4 /dev/urandom | xxd -p | tr -d '\n'
}

PASS=$(password)
zip -P "$PASS" $FILE.zip $FLAG_FILE || exit 1
echo "$PASS" >"$PASS_FILE"

for ((i=2; i <= $NUM; i++)); do
  NEWFILE="archive-revenge-$i"
  PASS=$(password)
  zip -P "$PASS" $NEWFILE.zip $FILE.zip "$PASS_FILE"
  echo "$PASS" >"$PASS_FILE"
  rm $FILE.zip
  FILE=$NEWFILE
done
