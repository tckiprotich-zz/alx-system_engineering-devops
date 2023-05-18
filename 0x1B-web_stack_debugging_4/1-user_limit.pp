# Change the OS configuration so that it is possible 
# to login with the holberton user and open
# a file without any error message.

# Create a file resource to ensure /etc/security/limits.d/holberton.conf exists
file { '/etc/security/limits.d/holberton.conf':
  ensure => 'file',
}

# Add the necessary limits to the holberton.conf file
file_line { 'increase-file-limits-for-holberton':
  path => '/etc/security/limits.d/holberton.conf',
  line => "holberton hard nofile 50000\nholberton soft nofile 50000",
}

# Ensure the limits.conf file includes holberton.conf
file_line { 'include-holberton-limits':
  path => '/etc/security/limits.conf',
  line => "## Include holberton limits\n@holberton -include /etc/security/limits.d/holberton.conf",
  match => '^## End of file$',
}
