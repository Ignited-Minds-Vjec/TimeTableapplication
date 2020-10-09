import urllib3
http = urllib3.PoolManager()
r = http.request('GET', 'https://vjec.acm.org/Data/share.txt')
print(r.data)