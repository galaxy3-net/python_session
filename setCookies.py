#!/usr/bin/python

import requests

setCookieURL = "https://httpbin.org/cookies"

cookies = {'location': 'Colorado'}

response = requests.get(setCookieURL, cookies=cookies)
print(response.text)
print(response.cookies)

setCookieURL = 'https://google.com'
cookieName = '1P_JAR'

response = requests.get(setCookieURL)
print(response.cookies[cookieName])
#print(response.text)
print(response.cookies)