# This class installs and configures the Apache HTTP server

class apache {
  # Install the httpd package
  package { 'httpd':
    ensure => installed,
  }

  # Create an index.html file with the 'Hello, world!' content
  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello, world!',
    owner   => 'apache',
    group   => 'apache',
    mode    => '0644',
  }

  # Start and enable the httpd service
  service { 'httpd':
    ensure => running,
