FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y
# Setup challenge environment
RUN apt-get install -y socat gcc-multilib

WORKDIR /challenge
COPY challenge /challenge

RUN chmod +x entrypoint.sh chall

USER nobody 

ENTRYPOINT ["./entrypoint.sh"]