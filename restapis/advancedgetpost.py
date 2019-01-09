## advanced guide on request lib
import requests
import urllib3

# review how json objects are accessed 

# dealing with session objs
session_cookie = 'https://httpbin.org/cookies/set/sessioncookie/123456789'
cookie = 'https://httpbin.org/cookies'
s = requests.Session()
s.get(session_cookie)
r = s.get(cookie)
#print(r.text)

def defualt_data():
    s = requests.Session
    s.auth = ('user','pass')
    s.headers.update({'x-test':'true'})

    # both x-t and x-t 2 are sent 
    s.get('https://httpbin.org/headers', headers={{'x-test2': 'true'}})




