#!/usr/bin/env python
from tasker import tasker

print tasker(4)
print tasker(4, smt=True)
print tasker(8, smt=True, cores=2, ways=4)

# invalid
print tasker(4, smt=True, cores=1, ways=2)
