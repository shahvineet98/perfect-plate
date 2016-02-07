#Gets the most visited pages with a valid API key
import requests
import json
from requests_oauthlib import OAuth1

zip_code = 20871
term = ""


# Pass term and zip code into url1 below
url1 = "https://api.yelp.com/v2/search?term=Starbucks&location=20871"
auth = OAuth1('CiC7-ll3e7KsXa6VBRD97Q','oeYypIyfVM7GrU4qgmoSn0unev4','SC5M3LImmeyhdW_ojNvWtvMhObbLTjkg','xEtFqALhn89vSN4Uh0CxLwBecBE')

yelpr = requests.get(url1.json(), auth=auth)


r=requests.get('http://api.reimaginebanking.com/merchants?key=36ad13980d64cfd6d1e2e561c370afa2').json()
frequencyArray={}
i=0
while i<len(r):
    if(r[i]['name'] in frequencyArray):
        frequencyArray[r[i]['name']]+=1
    else:
        frequencyArray[r[i]['name']]=1
    i+=1

maxCount=0
count=0
loopCount=0
while loopCount<5:
    for i in frequencyArray:
        count+=1
        if(frequencyArray[i]>maxCount):
            maxCount=frequencyArray[i]
            name=i
    maxCount=0
    loopCount+=1
    print(name)
    print(frequencyArray[name])
    frequencyArray[name]=0
