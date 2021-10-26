#AIDFHADISFHADISFH
file_line { 'cpk':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  line   => 'IdentityFile ~/.ssh/holberton',
  match  => 'IdentityFile ~/.ssh/holberton.pub',
}

file_line { 'np':
  ensure => present,
  path   => '/etc/ssh/ssh_config',
  match  => 'PasswordAuthentication yes',
  line   => 'PasswordAuthentication no',
}
