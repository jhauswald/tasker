#!/usr/bin/env python

def tasker(threads=2, cores=16, ways=2, smt=False):
  '''
  iterates over cores, threads, smt on same socket first
  '''

  if smt:
    assert(threads <= ways*cores)
  else:
    assert(threads <= cores)

  tid_cnt = 0
  cmd = 'tasket -c '
  if smt:
    for i in range(0, cores):
      for k in range(0, ways):
        tid = k*cores + i
        # last tid
        if tid_cnt + 1 == threads:
          cmd += str(tid)
          return cmd

        cmd += str(tid) + ','
        tid_cnt = tid_cnt + 1
  else:
    for i in range(0, threads):
      if tid_cnt + 1 == threads:
        cmd += str(i)
        return cmd

      cmd += str(i) + ','
      tid_cnt = tid_cnt + 1
