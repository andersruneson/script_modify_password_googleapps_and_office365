add this crontab for re-try send passwords again:

*/5 * * * * /usr/bin/python /script/try_again_O365.py

*/5 * * * * /usr/bin/python /script/try_again_google.py

posthock.sh the script can be added to self-service-password (http://ltb-project.org/wiki/documentation/self-service-password)
