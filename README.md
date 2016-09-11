add this crontab for re-try send passwords again:

*/5 * * * * /usr/bin/python /script/try_again_O365.py
*/5 * * * * /usr/bin/python /script/try_again_google.py
