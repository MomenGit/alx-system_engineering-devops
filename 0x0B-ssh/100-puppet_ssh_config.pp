# set up client SSH configuration file so that you can connect to a server
# without typing a password and sets IdentityFile ~/.ssh/school

file_line { '/etc/ssh/ssh_config':
  ensure => 'present',
  line   => '    PasswordAuthentication no'
}

file_line { '/etc/ssh/ssh_config':
  ensure => 'present',
  line   => '    IdentityFile ~/.ssh/school'
}
