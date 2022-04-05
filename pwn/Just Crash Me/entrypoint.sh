#!/bin/bash

socat -dd -T60 TCP-LISTEN:8000,reuseaddr,fork,su=StackSmasher EXEC:/home/StackSmasher/prog,stderr
