#!/usr/bin/env bash
# this script sets up web servers for deployment of web_static

# check if nginx is installed before trying to install
if ! command -v nginx &> /dev/null
then
	apt-get install nginx -y
fi

# create different folders if they don't exist
if [ ! -d /data/ ]
then
	mkdir /data/
fi

if [ ! -d /data/web_static/ ]
then
		mkdir /data/web_static/
fi

if [ ! -d /data/web_static/releases/ ]
then
	mkdir /data/web_static/releases/
fi

if [ ! -d /data/web_static/releases/test/ ]
then
		mkdir /data/web_static/releases/test/
fi

if [ ! -f /data/web_static/releases/test/index.html ]
then
	echo "This is tedious" > /data/web_static/releases/test/index.html
fi

# create symbolic link and recreate it every time the script is run
the_link="/data/web_static/current"
if [ -L "$the_link" ]
then
	rm "$the_link"
fi

# recreate it
ln -s "/data/web_static/releases/test/" "$the_link"

# change ownership of the data folder recursively
chown -R ubuntu:ubuntu /data/

# Define the paths and configuration file
nginx_config="/etc/nginx/sites-available/default"
web_static_dir="/data/web_static/current"

# Define the new location block
location_block="location /hbnb_static {
    alias $web_static_dir;
}"

# Check if the location block already exists in the configuration file
if grep -q "$location_block" "$nginx_config"; then
    echo "Location block already exists. Skipping..."
else
    # Add the location block to the configuration file using sed
    sudo sed -i "/server_name _;/a $location_block" "$nginx_config"
    echo "Location block added."
fi

# Restart Nginx
sudo systemctl restart nginx

