#!/usr/bin/python3

import sys, requests, getopt

print(sys.argv)
try:
    opts, args = getopt.getopt(sys.argv[1:], "l", ["location="])
except getopt.GetoptError:
    print('script.py -l location')
    sys.exit(2)

print("opts " + opts)
print("args " + args)
for opt, arg in opts:
    print("opt " + opt + "\n")
    print("arg " + arg + "\n")
    if opt in ("-l", "--location"):
        location = arg
        print("location is " + arg)

report =  open('output.txt', 'w')

setCookieURL = "https://httpbin.org/cookies"

cookies = {'location': location}

response = requests.get(setCookieURL, cookies=cookies)
print('Request 1: response.text' + "\n" +  response.text)
print('Request 1: response.cookies' + "\n")
print(response.cookies)

setCookieURL = 'https://google.com'
cookieName = '1P_JAR'

response = requests.get(setCookieURL)
print('Request 2: response.cookees[' + cookieName + "]\n" +  response.cookies[cookieName])
print('Request 2: response.text (see in output.txt' + "\n")
print(response.text, file=report)
print('Request 2: response.cookies' + "\n")
print(response.cookies)

report.close()

