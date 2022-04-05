FROM ubuntu:latest

RUN apt-get update && \
    DEBIAN_FRONTEND=noninteractive apt-get -y --no-install-recommends install openssh-server sudo cowsay && \
    rm -rf /var/lib/apt/lists/*

RUN useradd -m -d /home/ctf -s /bin/bash ctf && \
    useradd -m -d /home/ctf-cracked -s /bin/bash ctf-cracked && \
    echo 'ctf:832364048d291d45e26b8c77' | chpasswd && \
    usermod -aG sudo ctf

COPY challenge/flag.txt /flag.txt

RUN chmod 440 /flag.txt && \
    chown root:ctf-cracked /flag.txt

RUN ln -s /dev/null /home/ctf/.bash_history && \
    ln -s /dev/null /home/ctf-cracked/.bash_history

COPY challenge/perms /etc/sudoers

RUN chmod -r /tmp
ENTRYPOINT service ssh start && tail -f /dev/null
