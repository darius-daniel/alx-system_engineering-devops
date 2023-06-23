# A manifest that kill a process name 'killmenow'
exec { 'killmenow':
    command => '/usr/bin/pkill killmenow'
}
