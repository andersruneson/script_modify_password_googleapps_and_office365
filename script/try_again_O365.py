#!/usr/bin/python
import os
list = os.listdir('/password/office365')
for file in list :
    try:
        inside_file = open("/password/office365/%s" % file, "r")
        password = inside_file.read()
        inside_file.close()
        os.remove('/password/office365/%s' % file)
        os.system("python /script/office/officepassword.py %s %s" % (file,password))
    except:
      print('error')
