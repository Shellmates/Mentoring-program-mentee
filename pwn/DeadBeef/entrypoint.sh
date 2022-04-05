#!/bin/bash

socat -dd -T60 TCP-LISTEN:1337,reuseaddr,fork EXEC:/challenge/chall,stderr
