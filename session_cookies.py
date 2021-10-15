#!/usr/bin/python

import requests

session = requests.Session()

userName = {'userName': 'JSmith101'}
location = {'location': 'Colorado'}

setCookieUrl = 'https://httpbin.org/cookies/set'
getCookieUrl = 'https://httpbin.org/cookies'

session.get(setCookieUrl, param=userName)
session.get(setCookieUrl, param=location)

response = session.get(getCookieUrl)

print(response.text)
