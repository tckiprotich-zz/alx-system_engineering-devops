# This Puppet manifest installs and configures Apache on Ubuntu 14.04 LTS

# Install Apache package
package { 'apache2':
  ensure => installed,
}

# Configure Apache virtual host
file { '/etc/apache2/sites-available/my-site.conf':
  ensure => file,
  owner  => 'root',
  group  => 'root',
  mode   => '0644',
  content => template('apache/my-site.conf.erb'),
}

# Enable and start Apache virtual host
file { '/etc/apache2/sites-enabled/my-site.conf':
  ensure => link,
  target => '/etc/apache2/sites-available/my-site.conf',
}

# Restart Apache service
service { 'apache2':
  ensure    => running,
  enable    => true,
  hasrestart => true,
  hasstatus  => true,
  subscribe  => File['/etc/apache2/sites-enabled/my-site.conf'],
}
