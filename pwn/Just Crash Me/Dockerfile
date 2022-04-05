FROM ubuntu:18.04

RUN apt-get update && apt-get upgrade -y
RUN apt-get install -y socat --no-install-recommends

RUN useradd -ms /bin/sh StackSmasher

WORKDIR /home/StackSmasher


COPY ./flag.txt ./
COPY ./prog ./


RUN chown -R root:StackSmasher /home/StackSmasher && \
    chmod 750 /home/StackSmasher && \
    chown root:StackSmasher /home/StackSmasher/flag.txt && \
    chmod 440 /home/StackSmasher/flag.txt && \
    chmod 555 /home/StackSmasher/prog

EXPOSE 8000

COPY entrypoint.sh /
RUN chmod +x /entrypoint.sh
CMD ["/entrypoint.sh"]
