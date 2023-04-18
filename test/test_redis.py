import redis

r = redis.Redis(host='localhost', port=6379, db=1)

keys = r.scan_iter(match=':1:django.contrib.sessions.cache*')

for key in keys:
    value = r.get(key)
    print(key, value)
