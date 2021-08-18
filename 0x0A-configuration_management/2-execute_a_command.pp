# kill a

exec {'pkill':
  path     => ['/usr/bin'],
  command  => 'pkill killmenow',
  provider => 'shell',
}
