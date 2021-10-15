#!/usr/bin/python3

import sys, requests, getopt

try:
    opts, args = getopt.getopt(sys.argv[1:], "l:", ["location="])
except getopt.GetoptError:
    print('script.py -l location')
    sys.exit(2)

for opt, arg in opts:
    print("opt " + opt + "\n")
    print("arg " + arg + "\n")
    if opt in ("-l", "--location"):
        location = arg
        print("location is " + arg)

report =  open('output.txt', 'w')

setCookieURL = "https://httpbin.org/cookies"

cookies = {'location': location}

cookieJAR = requests.cookies.RequestsCookieJar()
cookieJAR.set("UserId", "JSmith101", domain="httpbin.org", path="/cookies")
cookieJAR.set("cartItem", "laptop", domain="httpbin.org", path="/cart")
cookieJAR.set("cookiecartItem", "laptop", domain="httpbin.org", path="/cookies")

response = requests.get(setCookieURL,cookies=cookieJAR)
print(response.text)

response = requests.get(setCookieURL,cart=cookieJAR)
print(response.text)
