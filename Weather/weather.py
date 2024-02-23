###Program Name: weather.py
###Programmer: Aaliyah Raderberg
###Project: Python Check Weather Forecast


##This as well only requires a single dependency.
#pip install requests


##Once installed just create a file to run with the script below.
import sys
import requests
resp = requests.get(f'https://wttr.in/{sys.argv[1].replace(" ", "+")}')
print(resp.text)


##After that, you are ready to run or schedule each day the following.
#python weather.py "Princeton, NJ"
