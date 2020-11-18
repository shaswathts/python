# coppied code

import urllib.request, urllib.parse, urllib.error, ssl
from bs4 import BeautifulSoup

start_url = input('Enter - ')
url_position = input('Enter position: ')
loop_count = input('Enter loop count: ')

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

cntr = 0

#print('Specified URL position:', url_position)
#print('First URL at Position:', start_url)

while cntr < int(loop_count):

    html = urllib.request.urlopen(start_url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')

    tags = soup('a')
    new_url = tags[int(url_position) - 1]
    start_url = new_url.get('href', None)

    #print('New URL: ', start_url)

    cntr = cntr + 1

final_url = start_url
print('Final URL:', final_url)

# My own code

import urllib.request, urllib.parse, urllib.error
from bs4 import BeautifulSoup
import ssl

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
pos = input('Enter position: ')
itr = input('Enter count: ')
ps = int(pos)
it = int(itr)
psq = 0
for i in range(it):
    html = urllib.request.urlopen(url, context=ctx).read()
    soup = BeautifulSoup(html, 'html.parser')
    tags = soup('a')
    for tag in tags:
        tag = tag.get('href', None)
        psq = psq + 1
        if ps == psq:
            url = tag
            psq = 0
            print('Retrieveing:',url)
        if psq == 0:
            break
