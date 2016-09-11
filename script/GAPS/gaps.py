#!/usr/bin/env python
import binascii
import quopri
import sys
import textwrap
import hashlib
import syslog
import json
import httplib2
import re
import os
import time

login = sys.argv[1]
newpassword = sys.argv[2]

fichier = open("/password/google/%s" % login , "a")
fichier.write(newpassword)
fichier.close()

from apiclient import errors
from apiclient.discovery import build
from oauth2client.client import SignedJwtAssertionCredentials

from ConfigParser import SafeConfigParser

## Get confgiruation
config = SafeConfigParser()
config.read('/script/GAPS/gaps.conf') 

## Load Google Configuration ##
with open( config.get('google', 'service_json')) as data_file:
  gaConfig = json.load(data_file)

## Load Google Service ##
def createDirectoryService(user_email):
  credentials = SignedJwtAssertionCredentials(
        gaConfig['client_email'],
        gaConfig['private_key'],
        scope='https://www.googleapis.com/auth/admin.directory.user',
        sub=user_email
  )

  http = httplib2.Http()
  http = credentials.authorize(http)

  return build('admin', 'directory_v1', http=http)


def update_password(mail, pwd):
    #ENCODE PASSWORD
    pwd = pwd.encode('ascii', 'ignore')
    password = hashlib.sha1(pwd).hexdigest()
    user = mail
    mail = mail + '@' +config.get('common', 'domain')

    # Create a new service object
    service = createDirectoryService(config.get('google', 'admin_email'))

    try:
        user = service.users().get(userKey = mail).execute()
    except:
        timevar = time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
        varloggaps = '%s Compte %s not found \n \n' % (timevar,mail)
        fichier = open("/var/log/gapslog.log", "a")
        fichier.write(varloggaps)
        fichier.close()
        return 0

    user['hashFunction'] = 'SHA-1'
    user['password'] = password

    try:
        #tentative envoie password
        service.users().update(userKey = mail, body=user).execute()
        #Write LOG
        timevar = time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
        varloggaps = '%s MAJ password for %s \n \n' % (timevar,mail)
        fichier = open("/var/log/gapslog.log", "a")
        fichier.write(varloggaps)
        fichier.close()
        os.remove('/password/google/%s' % login)
    except:
        #Write LOG ERROR 
        timevar = time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
        varloggaps = '%s echec de la mise a jour du mot de passe pour %s Same password ? \n \n' % (timevar,mail)
        fichier = open("/var/log/gapslog.log", "a")
        fichier.write(varloggaps)
        fichier.close()

update_password(mail=login,pwd=newpassword)
