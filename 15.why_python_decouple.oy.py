# https://github.com/henriquebastos/python-decouple/
# Decouple helps you to organize your settings so that you can change parameters without having to redeploy your app.

# It also makes it easy for you to:

# store parameters in ini or .env files;
# define comprehensive default values;
# properly convert values to the correct data type;
# have only one configuration module to rule all your instances.

# Usage
# pip install python-decouple

#Then use it on your settings.py.

#Import the config object:

from decouple import config
#Retrieve the configuration parameters:

SECRET_KEY = config('SECRET_KEY')
DEBUG = config('DEBUG', default=False, cast=bool)
EMAIL_HOST = config('EMAIL_HOST', default='localhost')
EMAIL_PORT = config('EMAIL_PORT', default=25, cast=int)

# Where the settings is used?
# https://github.com/henriquebastos/python-decouple/#where-is-the-settings-data-stored