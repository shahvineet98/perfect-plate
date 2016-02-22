#Gets the most visited pages with a valid API key
import requests
import json
from requests_oauthlib import OAuth1

zip_code = 20871
term = ""

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
topFive=[]
while loopCount<5:
    for i in frequencyArray:
        count+=1
        if(frequencyArray[i]>maxCount):
            maxCount=frequencyArray[i]
            name=i
    maxCount=0
    loopCount+=1
    topFive.append(name)
    #print(name)
    #print(frequencyArray[name])
    frequencyArray[name]=0
categories=[]
for i in range(5):
    miniCategoryList=[]
    # Pass term and zip code into url1 below
    url1 = "https://api.yelp.com/v2/search?term="+str(topFive[i])+"&location="+str(zip_code)
    auth = OAuth1('CiC7-ll3e7KsXa6VBRD97Q','oeYypIyfVM7GrU4qgmoSn0unev4','SC5M3LImmeyhdW_ojNvWtvMhObbLTjkg','xEtFqALhn89vSN4Uh0CxLwBecBE')

    yelpr = requests.get(url1, auth=auth).json()

    count=0
    
for i in yelpr['businesses'][9]['categories']:
    miniCategoryList.append(i[1])
    categories.append(miniCategoryList)
urlList=[]
for miniCategoryList in categories:
    url2 = "https://api.yelp.com/v2/search/?location="+str(zip_code)+"&category_filter="#+str(category)""
    for category in miniCategoryList:
        url2+=str(category)+","
    url2=url2[:len(url2)-1]
    urlList.append(url2)

recommendations=[]
ratings=[]
urls=[]
for urlLoc in range(5):
    query=requests.get(urlList[urlLoc],auth=auth).json()
    i=0
    val=5
    recommendationsMini=[]
    ratingsMini=[]
    urlMini=[]
    while i<val:
        try:
            if(query['businesses'][i]['name'] not in recommendations and query['businesses'][i]['name'] not in recommendationsMini):
                recommendationsMini.append(query['businesses'][i]['name'])
                ratingsMini.append(query['businesses'][i]['rating_img_url'])
                urlMini.append(query['businesses'][i]['url'])
            else:
                val+=1
            i+=1
        except:
            break
    recommendations.append(recommendationsMini)
print(categories)
print(recommendations)    
#print(query['businesses'][2]['name'])#['name'])
#url2 = "https://api.yelp.com/v2/search/?location="+str(zip_code)+"&category_filter="+str(category)""businesses
#print(categories)




