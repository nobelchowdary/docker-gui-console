#!/usr/bin/python3
import cgi
print("content-type: text/html")
print()
#print("hi LW")

import subprocess
o = subprocess.getoutput("sudo docker run -d=true centos:latest")
print(o)
