# Nginx install
package { 'nginx':
  ensure => installed,
}

file { 'index.html':
  ensure  => present,
  path    => '/var/www/html/index.html',
  content => 'Holberton School\n',
}

file_line { 'file':
  ensure => 'present',
  path   => '/etc/nginx/sites-available/default',
  after  => 'listen 80 default_server;',
  line   => 'rewrite ^/redirect_me https://www.youtube.com/watch?v=QH2-TGUlwu4 permanent;',
}

service { 'nginx':
  ensure     => running,
  enable     => true,
  hasrestart => true,
  require    => Package['nginx'],
  subscribe  => File_line['file'],
}