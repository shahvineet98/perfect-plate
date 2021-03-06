# We need to import request to access the details of the POST request
# and render_template, to render our templates (form and response)
# we'll use url_for to get some URLs for the app on the templates
from flask import Flask, render_template, request, url_for
import os
import requests
import json
from requests_oauthlib import OAuth1
zipcode=0
# Initialize the Flask application
def get_most_visited(enter):
    global zipcode
    zipcode = enter
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
        #print(frequencyArray[name])
        frequencyArray[name]=0
    return topFive
def recommendations(topFive):
    global zipcode
    categories=[]
    miniCategoryList=[]
        # Pass term and zip code into url1 below
    url1 = "https://api.yelp.com/v2/search?term="+str(topFive)+"&location="+str(zipcode)
    auth = OAuth1('CiC7-ll3e7KsXa6VBRD97Q','oeYypIyfVM7GrU4qgmoSn0unev4','SC5M3LImmeyhdW_ojNvWtvMhObbLTjkg','xEtFqALhn89vSN4Uh0CxLwBecBE')

    yelpr = requests.get(url1, auth=auth).json()

    count=0
    
    #for i in yelpr['businesses'][9]['categories']:
    miniCategoryList.append(yelpr['businesses'][9]['categories'])
    #categories.append(miniCategoryList)
    urlList=[]
    for i in miniCategoryList:
        print(i)
        url2 = "https://api.yelp.com/v2/search/?location="+str(zipcode)+"&category_filter="#+str(category)""
        for category in miniCategoryList:
            url2+=str(category)+","
        url2=url2[:len(url2)-1]
        urlList.append(url2)
    print(urlList)
    recommendations=[]
    ratings=[]
    urls=[]
    query=requests.get(urlList[0],auth=auth).json()
    i=0
    recommendationsMini=[]
    val=5
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
    print(categories)
    return recommendations


app = Flask(__name__)

# Define a route for the default URL, which loads the form
@app.route('/')
def form():
    return render_template('index.html')

# Define a route for the action of the form, for example '/hello/'
# We are also defining which type of requests this route is 
# accepting: POST requests in this case
@app.route('/hello/', methods=['POST'])
def hello():
    global zipcode
    zipcode=request.form['zipcode']
    names=get_most_visited(zipcode)
    #email=categories request.form['youremail']
    return render_template('category_listing.html',category1=names[0],category2=names[1],category3=names[2],category4=names[3],category5=names[4])

@app.route('/hello2/', methods=['POST'])
def hello2():
    #global zipcode
    name=get_most_visited(zipcode)[0]
    print(name)
    names=recommendations(name)
    return render_template('suggestions.html',recommend1=names[0],recommend2=names[1],recommend3=names[2],recommend4=names[3],recommend5=names[4])

@app.route('/hello3/', methods=['POST'])
def hello3():
    global zipcode
    name=get_most_visited(zipcode)[1]
    names=recommendations(name)
    return render_template('suggestions.html',recommend1=names[0],recommend2=names[1],recommend3=names[2],recommend4=names[3],recommend5=names[4])

@app.route('/hello4/', methods=['POST'])
def hello4():
    global zipcode
    name=get_most_visited(zipcode)[2]
    names=recommendations(name)
    return render_template('suggestions.html',recommend1=names[0],recommend2=names[1],recommend3=names[2],recommend4=names[3],recommend5=names[4])

@app.route('/hello5/', methods=['POST'])
def hello5():
    global zipcode
    name=get_most_visited(zipcode)[3]
    names=recommendations(name)
    return render_template('suggestions.html',recommend1=names[0],recommend2=names[1],recommend3=names[2],recommend4=names[3],recommend5=names[4])

@app.route('/hello6/', methods=['POST'])
def hello6():
    global zipcode
    name=get_most_visited(zipcode)[4]
    names=recommendations(name)
    return render_template('suggestions.html',recommend1=names[0],recommend2=names[1],recommend3=names[2],recommend4=names[3],recommend5=names[4])

# Run the app :)
if __name__ == '__main__':
    #Gets the most visited pages with a valid API key
    app.debug = True
    app.run()
