#!/usr/bin/python

import requests

report =  open('output.txt', 'w')

setCookieURL = "https://httpbin.org/cookies"

cookies = {'location': 'Colorado'}

response = requests.get(setCookieURL, cookies=cookies)
print('Request 1: response.text' + "\n" +  response.text)
print('Request 1: response.cookies' + "\n")
print(response.cookies)

setCookieURL = 'https://google.com'
cookieName = '1P_JAR'

response = requests.get(setCookieURL)
print('Request 2: response.cookees[' + cookieName + "]\n" +  response.cookies[cookieName])
print(response.text, file=report)
#print(response.text)
print('Request 2: response.cookies' + "\n")
print(response.cookies)

report.close()

