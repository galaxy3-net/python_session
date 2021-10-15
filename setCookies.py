#!/usr/bin/python

import requests

setCookieURL = "https://httpbin.org/cookies"

cookies = {'location': 'California'}

response = requests.get(setCookieURL, cookies=cookies)
print(response.text)