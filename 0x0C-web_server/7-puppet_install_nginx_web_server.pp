# A Puppet manifest to install and configure Nginx on a server

exec {'install':
  provider => bash,
  command  => 'sudo apt-get -y update ; sudo apt-get -y install nginx ; echo "Hello World!" | sudo tee /var/www/html/index.nginx-debian.html ; sudo sed -i "s/server_name _;/server_name _;\n\trewrite ^\/redirect_me https:\/\/google.com permanent;/" /etc/nginx/sites-available/default ; sudo service nginx start',
}
