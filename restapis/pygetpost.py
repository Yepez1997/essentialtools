import requests
import json

# request my git stuff 
time_line = 'https://api.github.com/events'
http_bin_get = 'https://httpbin.org/get'

user = "Yepez1997"
password = "Jrclass20160!"
r = requests.get('https://api.github.com/user',auth=(user,password))
#print(r.headers['content-type'])
#print(r.encoding)
# retrive events with response 
r2 = requests.get(time_line)

# passing key values 
kv = {'key1':'value1','key2':'value2', 'key3':'value3', 'key4':'value4'}
rkv = requests.get(http_bin_get, params=kv)
#print(r.url) # should retrieve url + kv

#print("       ")

kvlist = {'key1':'value1','key2':'value2', 'key3':['value4','value3']}
rlist = requests.get(http_bin_get, params=kvlist)
#print(rlist.url)

# git time line 
git_time_line = requests.get(time_line)
#print(git_time_line.text)
data = git_time_line.json()
#clearprint(data)

# raw content responses ie get raw socket response 
raw_request = requests.get(time_line, stream=True)
raw_raw = raw_request.raw

"""
with open(filename, 'wb') as fd:
    for chunk in r.iter_content(chunk_size=128):
        fd.write(chunk)
 *** -> use this to write the raw response        
"""
post = "https://httpbin.org/post"


post_request= requests.post(post, data=kv)
#print(post_request.text)

post_request_list = requests.post(post,data=kvlist)
#print(post_request_list.text)

# Want to assert tuples are same as key value 
tuple_pair = [('key1','val1'),('key1','val2')]
kv_pair =  {'key1' :['val1','val2']}

request_tuple = requests.post(post, data=tuple_pair)
request_list = requests.post(post, data=kv_pair)

assert(request_list.text == request_tuple.text)

# HEADERS 
print(rkv.headers['Content-Type'])






