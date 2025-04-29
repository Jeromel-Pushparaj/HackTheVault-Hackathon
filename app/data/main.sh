# Enabling Short open tag for PHP
sed -i "s/short_open_tag =.*/short_open_tag = On/" /etc/php/8.3/apache2/php.ini

# Installing Composer requires in root directory
cd /var/www/html/htdocs
composer require mongodb/mongodb


/usr/sbin/apache2ctl -D FOREGROUND