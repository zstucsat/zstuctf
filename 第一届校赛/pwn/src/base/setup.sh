#!/bin/bash

sed -i "s/http:\/\/archive.ubuntu.com/http:\/\/mirrors.163.com/g" /etc/apt/sources.list
sed -i "s/http:\/\/security.ubuntu.com/http:\/\/mirrors.163.com/g" /etc/apt/sources.list
apt-get update 
apt-get -y dist-upgrade
apt-get install -y xinetd lib32z1 lib32stdc++6 sudo
echo '[+] apt-get Done.'