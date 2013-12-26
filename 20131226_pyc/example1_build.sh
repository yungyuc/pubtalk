#!/bin/sh

cp example1.py /tmp/example1c.py
cython /tmp/example1c.py -o /tmp/example1c.c
gcc -O0 `python-config --includes` -c /tmp/example1c.c -fPIC -o /tmp/example1c.o
gcc `python-config --libs` /tmp/example1c.o -shared -o example1c.so
cython example1d.pyx -o /tmp/example1d.c
gcc -O0 `python-config --includes` -c /tmp/example1d.c -fPIC -o /tmp/example1d.o
gcc `python-config --libs` /tmp/example1d.o -shared -o example1d.so
