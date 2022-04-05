FROM ruby:3.0

COPY app /app

WORKDIR /app

RUN bundle install

RUN useradd ctf

USER ctf

EXPOSE 1337

ENTRYPOINT ["ruby", "app.rb"]
