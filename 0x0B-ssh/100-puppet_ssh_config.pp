# set up client SSH configuration file so that you can connect to a server
# without typing a password and sets IdentityFile ~/.ssh/school

file_line { 'Sets pw auth to no':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    PasswordAuthentication no'
}

file_line { 'Sets id file':
  ensure => 'present',
  path   => '/etc/ssh/ssh_config',
  line   => '    IdentityFile ~/.ssh/school'
}
