#!/bin/bash

leet_user=shellmates

echo "Enter your name:"
read name

if [ "$name" = "$leet_user" ]; then
  cat flag.txt
else
  echo "Access denied for $name"
fi
