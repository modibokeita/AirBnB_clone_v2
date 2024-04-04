# 5. Puppet for setup
# advanced
# Redo the task #0 but by using Puppet:

# Install nginx and configure server for serving web_static content
class web_static_setup {
  package { 'nginx':
    ensure => installed,
  }

  file { '/etc/nginx/sites-enabled/default':
    ensure  => present,
    content => template('nginx/default.erb'),
    notify  => Service['nginx'],
  }

  service { 'nginx':
    ensure    => running,
    enable    => true,
    subscribe => File['/etc/nginx/sites-enabled/default'],
  }

  file { '/data':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/shared':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test':
    ensure => directory,
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }

  file { '/data/web_static/releases/test/index.html':
    ensure  => present,
    content => '<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>',
    owner   => 'ubuntu',
    group   => 'ubuntu',
  }

  file { '/data/web_static/current':
    ensure => link,
    target => '/data/web_static/releases/test',
    owner  => 'ubuntu',
    group  => 'ubuntu',
  }
}

# Apply the class
include web_static_setup
