FROM php:7.2-apache
COPY challenge/ /var/www/html/
WORKDIR /var/www/html
RUN php setup.php && rm -f setup.php