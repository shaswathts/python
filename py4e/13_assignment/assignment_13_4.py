import urllib.request, urllib.parse, urllib.error
import json
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
uh = urllib.request.urlopen(url, context=ctx).read().decode()

info = json.loads(uh)
print('User count:', len(info))
#print(json.dumps(info, indent=4))
sum = 0
for item in info['comments']:
    x = item['count']
    sum = sum + x
print(sum)
