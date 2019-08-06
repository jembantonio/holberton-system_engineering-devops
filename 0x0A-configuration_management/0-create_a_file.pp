# Using Puppet, create a file in /tmp with requirements

file { '/tmp/holberton':
  ensure  => file,
  path 	  => '/tmp/holberton',
  mode 	  => '0744',
  owner	  => 'www-data',
  group	  => 'www-data',
  content => 'I love Puppet'
}
