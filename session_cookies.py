#!/usr/bin/python

import requests

session = requests.Session()

userName = {'userName': 'JSmith101'}
location = {'location': 'Colorado'}

setCookieUrl = 'https://httpbin.org/cookies/set'
getCookieUrl = 'https://httpbin.org/cookies'

session.get(setCookieUrl, params=userName)
session.get(setCookieUrl, params=location)

response = session.get(getCookieUrl)

print(response.text)

#  https://www.youtube.com/watch?v=8qsNauBEVNM
