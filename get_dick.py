#!/usr/bin/env python
from time import time

def get_dick(bytes=128):
  with open("/dev/urandom") as f:
    buffer = ""
    start_time = time()
    while "dick" not in str(buffer):
      buffer = f.read(bytes)
    total_time = time() - start_time
    print("It took %s seconds to find 'dick' in %s bytes of /dev/urandom." % (total_time,bytes))
    print(str(buffer))
    print("You're welcome.")

if __name__ == "__main__":
  get_dick()
