# A Puppet manifest to install and configure Nginx on a server
package { 'puppet':
    ensure   => 'installed'
    provider => 'apt',
}

exec { 'puppetlabs-nginx':
    commad => 'puppet module install puppetlabs-nginx'
}

class { 'nginx':
    ensure  => 'installed',
    service => 'running',
}

nginx::resource::vhost { 'dariusdaniel.tech':
    ensure      => present,
    www_root    => '/var/www/html',
    listen_port => '80'
    index_files => ['index.nginx-debian.html']
}
