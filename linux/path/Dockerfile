FROM ubuntu:latest

RUN apt-get update && \
    apt-get install -y openssh-server python3 sudo


RUN useradd -s /bin/bash ch3
RUN useradd -s /bin/bash ch3-cracked
RUN echo 'ch3:ctf' | chpasswd
RUN usermod -aG sudo ch3

RUN chmod -r /tmp 
RUN chmod -r /var/tmp 

COPY challenge/flag.txt /flag
COPY challenge/perms /etc/sudoers
COPY challenge/my_ls /my_ls


RUN chown  root:ch3-cracked /flag
RUN chmod 550 /flag

RUN chown  root:ch3-cracked /my_ls
RUN chmod 555 /my_ls

EXPOSE 22


ENTRYPOINT service ssh start && tail -f /dev/null
