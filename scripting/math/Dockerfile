FROM ubuntu:20.04


RUN apt-get update && apt-get upgrade -y

# Setup challenge environment
RUN apt-get install -y socat python3 python3-pip --no-install-recommends
RUN python3 -m pip install ecdsa

WORKDIR /challenge
COPY challenge /challenge
RUN chmod +x entrypoint.sh chall.py

USER nobody 

ENTRYPOINT ["./entrypoint.sh"]