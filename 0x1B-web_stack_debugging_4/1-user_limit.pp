# Change the OS configuration so that it is possible 
# to login with the holberton user and open
# a file without any error message.

# Create the holberton user

user { 'holberton':
  ensure => present,
}

# Allow login for the holberton user
file { '/etc/ssh/sshd_config':
  ensure  => present,
  owner   => 'root',
  group   => 'root',
  mode    => '0644',
  content => file('/etc/ssh/sshd_config').content + "
Match User holberton
    PasswordAuthentication yes
",
  notify  => Service['sshd'],
}

# Open a file without error messages
file { '/path/to/your/file':
  ensure  => present,
  owner   => 'holberton',
  group   => 'holberton',
  mode    => '0644',
  content => 'Content of your file',
}

# Restart the SSH service
service { 'sshd':
  ensure    => running,
  enable    => true,
  hasstatus => true,
  restart   => '/usr/sbin/service sshd reload',
  require   => File['/etc/ssh/sshd_config'],
}
