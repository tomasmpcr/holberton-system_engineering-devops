# Add heder in pp, install nginx and add header

exec { 'update':
  command => '/usr/bin/apt update',
}

package { 'nginx':
    ensure  => present,
    require => Exec['update'],
}

file_line {'add_header':
    ensure  => 'present',
    path    => '/etc/nginx/sites-available/default',
    after   => 'listen 80 default_server;',
    line    => 'add_header X-Served-By $hostname;',
    require => Package['nginx'],
}

service { 'nginx':
    ensure  => running,
    require => File_line['add_header'],
}

