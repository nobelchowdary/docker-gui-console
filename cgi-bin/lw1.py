#!/usr/bin/python3
import cgi
print("content-type: text/html")
print()
#print("hi LW")

import subprocess
f = cgi.FieldStorage()
cmd = f.getvalue("x")
o = subprocess.getoutput("sudo docker " + cmd )
print(o)
