#How long does it take to find 'dick' in 128 bytes at a time of /dev/urandom?

Just run `python get_dick.py` and find out.

You can also supply a byte integer amount, like `python get_dick.py 32`, to search in smaller or larger byte sets.

#Can I use get_dick elsewhere?

Sure! Just `from get_dick import get_dick` and call. You'll be returned a tuple of `(buffer,total_time)`.
