import requests
import json

#https://shop.lululemon.com/api/s?Ntt=running&page[offset]=0

url_api = "https://shop.lululemon.com/api/s"

#this is a function
#something has to call the function for it to execute
def makRequest(searchTerm):
    headers = {'User-Agent': "PostmanRuntime/7.15.2",'Accept': "*/*",'Cache-Control': "no-cache",'Accept-Encoding': "gzip, deflate",'Connection': "keep-alive",'cache-control': "no-cache"}
    querystring = {"Ntt":"running","page[offset]":0}
    response = requests.request("GET", url_api, headers=headers, params=querystring)
    result_json = json.loads(response.text)
    print(result_json)

#2 dictionaries that we'll use for searching fashionnova
#both dictionaries have different formatting. both formats are OK
#1 dictionary has good qualities
#1 dictionary has the qualities of a loser
positive = {
    'strong',
    'athletic',
    'work'
}

negative = {'overweight','lazy'}

#loop through all the negative terms and search fashionnova
for searchTerm in negative:
    print("\n Category: negative\t Search Term " + searchTerm)
    #this calls the function called makeRequest, which we've defined at the top
    makRequest(searchTerm)


#loop through all the positive terms and search fashionnova
for searchTerm in positive:
    print("\n Category: positive\t Search Term " + searchTerm)
    #this calls the function called makeRequest, which we've defined at the top
    makRequest(searchTerm)
