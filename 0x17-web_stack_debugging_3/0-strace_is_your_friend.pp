# A manifest that fixes a 500 error return by an Apache server

exec { 'fix-wordpress':
  provider => shell,
  command  => 'sed -i "s/phpp/php/g" /var/www/html/wp-settings.php'
}
