import urllib.request, urllib.parse, urllib.error
import xml.etree.ElementTree as ET
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter location: ')
html = urllib.request.urlopen(url, context=ctx).read()
tree = ET.fromstring(html)
find = tree.findall('.//count')
print('count list:', len(find))
sum = 0
for item in find:
    sum = sum + int(item.text)
print(sum)
