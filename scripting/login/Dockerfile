FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y socat && \
    rm -rf /var/lib/apt/lists/*

RUN useradd ctf && \
    mkdir /challenge

COPY entrypoint.sh flag.txt login.sh /challenge/

WORKDIR /challenge

RUN chmod +x login.sh entrypoint.sh 

ENTRYPOINT ["./entrypoint.sh"]
