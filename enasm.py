#!/usr/bin/env python2.7
import subprocess
import os
import sys
filename = sys.argv[1]
subprocess.call("nasm -f elf64 "+filename,shell=True)
subprocess.call("ld -s -o "+filename[:-4]+" "+filename[:-4]+".o",shell=True)
arguments=""
for argv in sys.argv[2:]:
	arguments=arguments+" "+argv
subprocess.call("./"+filename[:-4]+" "+arguments,shell=True)


