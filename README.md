Script modify password googleapps and office365
====

Installation
======

Google Apps
=========
1.Install python-pip
2. Create a project in Google Developer Console and ad Admin SDK permission
3.Create a JSON config for you project in Google Developer Console
4.Download the json config from the Google Developer Console to your samba machine and replace json
5.pip install --upgrade google-api-python-client
6.Edit gaps.conf 

add crontab
====
add this crontab for re-try send passwords again:

*/5 * * * * /usr/bin/python /script/try_again_O365.py

*/5 * * * * /usr/bin/python /script/try_again_google.py

posthock.sh the script can be added to self-service-password (http://ltb-project.org/wiki/documentation/self-service-password)
