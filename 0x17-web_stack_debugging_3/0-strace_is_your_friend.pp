class apache {
  package { 'httpd':
    ensure => installed,
  }

  file { '/var/www/html/index.html':
    ensure  => file,
    content => 'Hello, world!',
    owner   => 'apache',
    group   => 'apache',
    mode    => '0644',
  }

  service { 'httpd':
    ensure => running,
    enable => true,
  }
}
