FROM ubuntu:18.04

RUN apt-get update && \
    apt-get install -y socat python3 gcc cron nano && \
    rm -rf /var/lib/apt/lists/* 

RUN useradd -s /bin/bash ctf
RUN useradd -s /bin/bash linus


# CRON 
COPY clean /usr/bin
RUN chmod 700 /usr/bin/clean

RUN crontab -l | { cat; echo "*/5 * * * * /bin/bash /usr/bin/clean"; } | crontab -
RUN cron
# CRON END

COPY entrypoint.sh .

COPY flag.txt . 
COPY challenge/info .
COPY challenge/run chall
COPY challenge/run.c chall.c


RUN chown root:linus flag.txt
RUN chmod 440 flag.txt

RUN chown root:root chall.c
RUN chmod 755 chall.c

RUN chown root:root info
RUN chmod 775 info

RUN chown root:linus chall
RUN chmod 755 chall

RUN chmod g+s chall

RUN chmod -r /tmp 

USER ctf 


ENTRYPOINT ["/entrypoint.sh"]
