#!/usr/bin/env python
from time import time

def get_dick(bytes=128):
  with open("/dev/urandom") as f:
    buffer = ""
    start_time = time()
    while "dick" not in str(buffer):
      buffer = f.read(bytes)
    total_time = time() - start_time
  return (buffer,total_time)

if __name__ == "__main__":
  import sys
  bytes = 128
  try:
    bytes = int(sys.argv[1])
  except:
    pass
  buffer, total_time = get_dick(bytes)
  print("It took %s seconds to find 'dick' in %s bytes of /dev/urandom." % (total_time,bytes))
  print(str(buffer))
  print("You're welcome.")
