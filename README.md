Script modify password googleapps and office365
====

Installation
======

Google Apps
=========
1.Install python-pip

2.Create a project in Google Developer Console and ad Admin SDK permission
 
3.Create a JSON config for you project in Google Developer Console

4.Download the json config from the Google Developer Console to your samba machine and replace json

5.pip install --upgrade google-api-python-client

6.Edit gaps.conf 


Office 365
=========
1.Create your domaine in "windows azure"

2.git clone git://github.com/Azure/azure-sdk-for-python.git

3.cd azure-sdk-for-python

4.python setup.py install

5.Replace username and password in officepassword.py and replace your domain

Add this crontab for re-try send passwords again:
====
*/5 * * * * /usr/bin/python /script/try_again_O365.py

*/5 * * * * /usr/bin/python /script/try_again_google.py

posthock.sh the script can be added to self-service-password (http://ltb-project.org/wiki/documentation/self-service-password)
