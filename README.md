# django_slack
# Config Django

* Append 'django\_slack' to INSTALLED\_APPS;
* Append 'django\_slack.urls' to urls;

# Append Command

1. Access your django's admin, find 'django\_slack';
2. Add a new command, and paste your code which contains a function named 'command\_func' into the `code` field, fill the `command` field the literal command value, such as 'hello\_world', and the slack command url will be the 'host/slack\_cli/hello\_world/'

# Config slack

Fill the `url` field with the command url
# Triggle the command

Type the command in slack, and slack will call the given command url.
