#!/bin/sh

cython example2d.pyx -o /tmp/example2d.c
gcc -O0 `python-config --includes` -c /tmp/example2d.c -fPIC -o /tmp/example2d.o
gcc `python-config --libs` /tmp/example2d.o -shared -o example2d.so
cython example2a.pyx -o /tmp/example2a.c
gcc -O0 `python-config --includes` -c /tmp/example2a.c -fPIC -o /tmp/example2a.o
gcc `python-config --libs` /tmp/example2a.o -shared -o example2a.so
cython example2b.pyx -o /tmp/example2b.c
gcc -O0 `python-config --includes` -c /tmp/example2b.c -fPIC -o /tmp/example2b.o
gcc `python-config --libs` /tmp/example2b.o -shared -o example2b.so
gcc -O0 -std=c99 -c example2.c -o /tmp/example2.o
cython example2c.pyx -o /tmp/example2c.c
gcc -O0 `python-config --includes` -c /tmp/example2c.c -fPIC -o /tmp/example2c.o
gcc `python-config --libs` /tmp/example2.o /tmp/example2c.o -shared -o example2c.so
