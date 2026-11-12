#!/bin/bash



cmake -S bridge/. -B build

cmake --build build

# Apparently, the & makes the shell script start them simultaneously
./build/bridge &
./basilisk_env/bin/python FirstBasiliskSimulation.py
