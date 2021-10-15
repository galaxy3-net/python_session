#!/usr/bin/python

import requests

setCookieURL = "https://httpbin.org/cookies"

cookies = {'location': 'Colorado'}

response = requests.get(setCookieURL, cookies=cookies)
print(response.text)