#!/bin/bash -ex

# https://github.com/zardus/ctf-tools/blob/master/stegsolve/install
wget http://www.caesum.com/handbook/Stegsolve.jar -O stegsolve.jar
chmod +x stegsolve.jar
mkdir bin
mv stegsolve.jar bin/