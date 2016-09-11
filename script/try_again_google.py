#!/usr/bin/python
import os
list = os.listdir('/password/google')
for file in list :
    try :
      inside_file = open("/password/google/%s" % file, "r")
      password = inside_file.read()
      inside_file.close()
      os.remove('/password/google/%s' % file)
      os.system("python /script/GAPS/gaps.py %s %s" % (file,password))
    except:
      print('error')
