#!/usr/bin/python3
import cgi
print("content-type: text/html")
print()
#print("hi LW")

import subprocess
o = subprocess.getoutput("sudo docker rm -f $(docker ps -a -q)")
print(o)
