# django_slack
# Config Django
* Append 'django\_slack' to INSTALLED\_APPS;
* Include 'django\_slack.urls' to urls;
# Append Command
Access your django's admin, find the 'django\_slack', add a new command, and paste your code which contains a function named 'command\_func' into the `code` field, fill the `command` field the literal command value, such as 'hello\_world', and the slack command url will be the 'host/slack\_cli/hello\_world/'
# Config slack
Fill the `url` field with the command url
# Triggle the command
Type the command in slack, and slack will call the give command url.
