from urllib.request import urlopen
from bs4 import BeautifulSoup
import ssl

#setting up the counter
sum = 0

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urlopen(url, context=ctx).read()
soup = BeautifulSoup(html, "html.parser")

# Retrieve all of the anchor tags
tags = soup('span')
for tag in tags:
    # Look at the parts of a tag
#    print('TAG:', tag)
#    print('URL:', tag.get('href', None))
    num = int(tag.contents[0])
    sum = num + sum
print('Total:', sum)
#    print('Attrs:', tag.attrs)
