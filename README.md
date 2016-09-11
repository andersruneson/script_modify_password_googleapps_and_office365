Script modify password googleapps and office365
====

Installation
======

Google
=========
Install python-pip
Create a project in Google Developer Console and ad Admin SDK permission
Create a JSON config for you project in Google Developer Console
Download the json config from the Google Developer Console to your samba machine and replace json
pip install --upgrade google-api-python-client
Edit gaps.conf 

add crontab
====
add this crontab for re-try send passwords again:

*/5 * * * * /usr/bin/python /script/try_again_O365.py

*/5 * * * * /usr/bin/python /script/try_again_google.py

posthock.sh the script can be added to self-service-password (http://ltb-project.org/wiki/documentation/self-service-password)
