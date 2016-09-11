#!/usr/bin/python
import sys 
import time
import os
from azure.common.credentials import ServicePrincipalCredentials
from azure.common.credentials import UserPassCredentials
from azure.graphrbac.models import PasswordProfile, UserUpdateParameters
from azure.graphrbac import GraphRbacManagementClient

login = sys.argv[1]
newpassword = sys.argv[2]
fichier = open("/password/office365/%s" % login , "a")
fichier.write(newpassword)
fichier.close()



email = login + '@lesfourmisduweb.org'


try :
   credentials = UserPassCredentials(
    'admin@lesfourmisduweb.org', 'mypassword', resource="https://graph.windows.net"
   )
except:
        timevar = time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
        varloggaps = '%s ERROR: Fail connexion credentials. Mail : %s  \n \n' % (timevar,email)
        fichier = open("/var/log/azurelog.log", "a") 
        fichier.write(varloggaps)
        fichier.close()


tenant_id = "e53e167a-e2bc-40ef-9b3f-fd6e9f999999"

graphrbac_client = GraphRbacManagementClient(
       credentials,
       tenant_id
)

param =         UserUpdateParameters(
                password_profile=PasswordProfile(
                    password=newpassword,
                    force_change_password_next_login=False
                )
                )

try :
        timevar = time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
        varloggaps = '%s INFO: send password for Mail : %s  \n \n' % (timevar,email)
        fichier = open("/var/log/azurelog.log", "a") 
        fichier.write(varloggaps)
        fichier.close()
        user = graphrbac_client.users.update(email, param)
        os.remove('/password/office365/%s' % login)


except:
        timevar = time.strftime('%d/%m/%y %H:%M:%S',time.localtime())
        varloggaps = '%s ERROR: Fail send password. Mail : %s  \n \n' % (timevar,email)
        fichier = open("/var/log/azurelog.log", "a") 
        fichier.write(varloggaps)
        fichier.close()
        print('ERROR : Fail send password for %s' % email)
