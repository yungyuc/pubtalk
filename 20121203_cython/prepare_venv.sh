#!/bin/sh

mkdir -p tmp
cd tmp
rm -rf cpython
virtualenv --system-site-package --setuptools cpython
. cpython/bin/activate
easy_install --upgrade cython
