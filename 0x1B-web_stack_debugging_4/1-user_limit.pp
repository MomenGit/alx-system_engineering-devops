# Change the OS configuration so that it is possible to login with
# the holberton user and open a file without any error message.

exec { 'allow holberton user':
  command => 'sed -i "s/holberton//" /etc/security/limits.conf',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
