# set up client SSH configuration file so that you can connect to a server
# without typing a password and sets IdentityFile ~/.ssh/school

file_line {'Sets pw auth to no':
  path   =>'/etc/ssh/ssh_config'
  ensure => 'present',
  line   => '    PasswordAuthentication no'
}

file_line { 'Sets id file':
  path   =>'/etc/ssh/ssh_config'
  ensure => 'present',
  line   => '    IdentityFile ~/.ssh/school'
}
