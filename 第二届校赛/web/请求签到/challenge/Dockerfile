FROM ubuntu:14.04

MAINTAINER Hn13 <root@hn13.top>
COPY ./file/sources.list /etc/apt/sources.list
# APT 自动安装 PHP 相关的依赖包，如需其他依赖包在此添加
RUN apt-get update \
    && apt-get -y install \
        curl \
        wget \
        apache2 \
        libapache2-mod-php5 \
        php5-gd \
        php5-curl \
        php-pear \
        php-apc \

    # 用完包管理器后安排打扫卫生可以显著的减少镜像大小
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && sed -i "s/AllowOverride None/AllowOverride All/g" /etc/apache2/apache2.conf \
    && sed -i "s/Require all denied/Require all granted/g" /etc/apache2/apache2.conf \
    && sudo ln -s /etc/apache2/mods-available/rewrite.load /etc/apache2/mods-enabled/rewrite.load \
    && rm /var/www/html/index.html
COPY ./file/index.php /var/www/html/index.php
COPY ./file/.htaccess /var/www/html/.htaccess
EXPOSE 80
CMD apachectl -D FOREGROUND
