FROM ubuntu:latest
ARG DEBIAN_FRONTEND=noninteractive
WORKDIR /var/app

RUN apt-get update
RUN apt upgrade -y
RUN apt install -y apache2
RUN apt install nano git -y

RUN apt install -y php libapache2-mod-php php-mysql
RUN apt install -y  php-pear php-dev

RUN pecl install mongodb
RUN echo "extension=mongodb.so" > /etc/php/8.3/apache2/conf.d/20-mongodb.ini
RUN echo "extension=mongodb.so" > /etc/php/8.3/cli/conf.d/20-mongodb.ini

RUN apt install -y python3 python3-pip 

RUN apt-get install -y certbot python3-certbot-apache apache2
RUN apt-get install curl
RUN curl -sS https://getcomposer.org/installer | php -- --install-dir=/usr/local/bin --filename=composer
RUN rm -rf /var/www/html
COPY ./data/ .
RUN chmod +x /var/app/main.sh

# RUN chmod +x /var/app/certificate.sh
RUN cp YOUR_SITE_CONFIG.conf /etc/apache2/sites-available/
RUN a2dissite 000-default.conf

#RUN rm /etc/apache/sites-available/000-default.conf
RUN a2ensite YOUR_SITE_CONFIG.conf
RUN a2enmod rewrite
VOLUME ["/var/www/html"]

# docker run -p 8080:80 -v D:\playground\index.html:/var/www/html jeromelpushparaj/apache2:local
CMD /var/app/main.sh