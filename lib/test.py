pinned_cpus="1,2,3"
port_number=9086
ideal_mem=2048

procs_path="/path/to/process"

prefix = 'echo $$ > {} &&'
memcached_serv = "/usr/bin/time -v memcached -l localhost -p {} -m {} -t 1".format(port_number,
                                                                                   ideal_mem)
# e.g. echo && > {} && exec taskset -c [cpu_list] /usr/bin/time -v memcached -l local -p [port] -m [ideal_mem] -t 1
cpu_list = list(pinned_cpus)
taskset_serv = 'taskset -c {}'.format(cpu_list[0])
memcached_serv = ' '.join((prefix, 'exec', taskset_serv, memcached_serv))
memcached_serv = memcached_serv.format(procs_path)

print(memcached_serv)