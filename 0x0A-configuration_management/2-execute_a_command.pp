# kills a process named killmenow

exec { 'kil_killmenow':
  command => 'pkill killmenow',
  path    => ['/bin', '/usr/bin']
}
