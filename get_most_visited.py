#Gets the most visited pages with a valid API key
import requests
import json
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
