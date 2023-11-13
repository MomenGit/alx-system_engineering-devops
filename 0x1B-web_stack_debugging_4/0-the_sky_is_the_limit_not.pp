# Restart Nginx server to fix too many open files error

exec { 'restart-nginx':
  command => 'sudo nginx -s stop && sudo nginx',
  path    => '/usr/sbin/nginx'
}
