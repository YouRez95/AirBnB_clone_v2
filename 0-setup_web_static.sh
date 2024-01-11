#!/usr/bin/env bash
#
sudo apt-get -y install nginx > /dev/null
mkdir -p /data/web_static/releases/test/
mkdir -p /data/web_static/shared/
echo "Hello World" > /data/web_static/releases/test/index.html
ln -sf /data/web_static/releases/test/ /data/web_static/current
chown -R ubuntu:ubuntu /data/
location="server_name _;\n\tlocation /hbnb_static {\n\t\talias /data/web_static/current/;\n\t}"
sed -i "s,server_name _;,$location," /etc/nginx/sites-available/default
service nginx restart
