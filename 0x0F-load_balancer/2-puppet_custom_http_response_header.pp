# Add heder in pp

exec { 'update':
  command => '/usr/bin/apt update',
}

package { 'nginx':
    ensure  => installed,
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
    command => 'sudo /usr/bin/service nginx restart',
    require => File_line['add_header'],
}
