FROM ubuntu:14.04

MAINTAINER Hn13 <root@hn13.top>
COPY ./file/sources.list /etc/apt/sources.list
# APT 自动安装 PHP 相关的依赖包，如需其他依赖包在此添加
RUN apt-get update \
    && apt-get -y install \
        mysql-server \
        curl \
        wget \
        apache2 \
        libapache2-mod-php5 \
        php5-gd \
        php5-curl \
        php5-mysqlnd \
    # 用完包管理器后安排打扫卫生可以显著的减少镜像大小
    && apt-get clean \
    && apt-get autoclean \
    && rm -rf /var/lib/apt/lists/* /tmp/* /var/tmp/* \
    && mkdir /var/www/html/file \
    && rm /var/www/html/index.html 
COPY ./file/index.php /var/www/html/index.php
COPY ./file/login.php /var/www/html/login.php
COPY ./file/F14ghgng1g3g.php /var/www/html/F14ghgng1g3g.php
COPY ./file/robots.txt /var/www/html/robots.txt
COPY ./file/sql.php /var/www/html/file/sql.php
COPY ./file/secret.php /var/www/html/file/secret.php
COPY ./file/php.ini /etc/php5/apache2/php.ini
COPY ./file/my.cnf /etc/mysql/my.cnf
COPY ./file/users.sql /tmp/users.sql
COPY ./file/flag /flag
COPY ./file/start.sh /start.sh
ENV MYSQL_ALLOW_EMPTY_PASSWORD yes
RUN usermod -d /var/lib/mysql/ mysql \
    && ln -s /var/lib/mysql/mysql.sock /tmp/mysql.sock \
    && chown -R mysql:mysql /var/lib/mysql \
    && service mysql restart \
    && sleep 3 \
    && mysql < /tmp/users.sql \
    && rm -rf /tmp/users.sql \
    && chmod +x /start.sh

EXPOSE 80
EXPOSE 3306
CMD /start.sh
