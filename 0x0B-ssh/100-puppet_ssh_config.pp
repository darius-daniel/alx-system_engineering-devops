# A Puppet manifest that makes changes to our configuration file.

$str => "Include /etc/ssh/ssh_config/d/*.conf
Host *
PasswordAuthentication yes
SendEnv LANG LC_*
HashKnownHosts yes
GSSAPIAuthentication yes
"

file { '/etc/ssh/ssh_config':
    ensure  => file,
    content => $str
    owner   => 'ubuntu',
    group   => 'ubuntu',
    mode    => '0744',
}
