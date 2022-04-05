FROM python:3.8-alpine

RUN apk update && apk add python3 socat

RUN adduser -h /home/ctf --disabled-password ctf

WORKDIR /home/ctf

COPY challenge/challenge.py .
COPY entrypoint.sh .

RUN chmod +x entrypoint.sh challenge.py

USER ctf

EXPOSE 1337

ENTRYPOINT [ "./entrypoint.sh" ]
