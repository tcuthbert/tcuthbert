class python_runtime () inherits ::tombomation {

  notify($dev)
  class { 'python' :
    version  => '3.4.1',
    pip      => true,
    gunicorn => true,
  }
}
