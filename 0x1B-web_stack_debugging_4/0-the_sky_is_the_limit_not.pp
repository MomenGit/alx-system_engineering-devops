# Restart Nginx server to fix too many open files error

exec { 'restart-nginx':
  command => 'nginx -s stop && nginx',
  path    => ['/bin', '/usr/bin', '/usr/sbin']
}
