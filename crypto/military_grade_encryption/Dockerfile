FROM ruby:latest

RUN useradd -ms /bin/sh aes_ecb_user

WORKDIR /home/aes_ecb_user


COPY ./challenge/* ./


RUN chown -R root:aes_ecb_user /home/aes_ecb_user && \
    chmod 750 /home/aes_ecb_user && \
    chown root:aes_ecb_user /home/aes_ecb_user/flag.txt && \
    chmod 440 /home/aes_ecb_user/flag.txt && \
    chmod 555 /home/aes_ecb_user/prog.rb

EXPOSE 137

CMD ["ruby","/home/aes_ecb_user/prog.rb"]
