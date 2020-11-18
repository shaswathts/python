import urllib.request, urllib.parse, urllib.error
import json
import ssl

#you only use this part if you have a API key obtained from the producer

#api_key = False
# If you have a Google Places API key, enter it here
# api_key = 'AIzaSy___IDByT70'
# https://developers.google.com/maps/documentation/geocoding/intro

#if api_key is False:
#    api_key = 42
#    serviceurl = 'http://py4e-data.dr-chuck.net/json?'
#else :
#    serviceurl = 'https://maps.googleapis.com/maps/api/geocode/json?'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

# or if you dont have a original google API key you can use a subset of googleAPI written by Dr chuck bellow is the url and code part

api_key = 42
service_url = 'http://py4e-data.dr-chuck.net/json?'
while True:
    address = input('Enter location: ')
    if len(address) < 1: break

    parms = dict()
    parms['address'] = address
#    and also the bello code is when you have a API key from producer
#    if api_key is not False: parms['key'] = api_key
#    if you dont have a API key you can instead use this code bellow
    parms['key'] = api_key
    url = serviceurl + urllib.parse.urlencode(parms)

    print('Retrieving', url)
    uh = urllib.request.urlopen(url, context=ctx)
    data = uh.read().decode()
    print('Retrieved', len(data), 'characters')

    try:
        js = json.loads(data)
    except:
        js = None

    if not js or 'status' not in js or js['status'] != 'OK':
        print('==== Failure To Retrieve ====')
        print(data)
        continue

    print(json.dumps(js, indent=4))

    lat = js['results'][0]['geometry']['location']['lat']
    lng = js['results'][0]['geometry']['location']['lng']
    print('lat', lat, 'lng', lng)
    location = js['results'][0]['formatted_address']
    print(location)
