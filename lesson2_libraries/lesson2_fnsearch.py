import requests
import json

#this program will make API requests to fashionnova based on a search term
#the final URL will look something like this where the parameter "q" is the search term
#https://premium-fnova-dot-acp-magento.appspot.com/?q=work&s=www.fashionnova.com&cdn_cache_key=1566483085&v=5.672.066&store_id=2939277&UUID=8fb37bd6-aef1-4d7c-be3f-88bafef01308&callback=acp_magento_acp_new2

#define the variables
url_api = "https://premium-fnova-dot-acp-magento.appspot.com/"
url_fn = 'https://www.fashionnova.com'
url_fn_search = url_fn + '/pages/search-results?q='

#this is a function
#something has to call the function for it to execute
def makRequest(searchTerm):
    #don't worry about this. It is needed to make a web http request
    headers = {'User-Agent': "PostmanRuntime/7.15.2",'Accept': "*/*",'Cache-Control': "no-cache",'Host': "premium-fnova-dot-acp-magento.appspot.com",'Accept-Encoding': "gzip, deflate",'Connection': "keep-alive",'cache-control': "no-cache"}
    
    querystring = {"q":searchTerm,"s":"www.fashionnova.com","cdn_cache_key":"1566483085","UUID":"8fb37bd6-aef1-4d7c-be3f-88bafef01308"}
    response = requests.request("GET", url_api, headers=headers, params=querystring)
    result_json = json.loads(response.text)
    counter = 0
    items = result_json['items']
    while result_json['total_results']>0 and counter<2:
        item = items[counter]
        productUrl = url_fn + item['u']
        print(str(counter)+": " + searchTerm + "\t" + item['l'] + "\tPrice: " + item['p'] + "\tProduct URL: " + productUrl +"\tImage URL : " + item['t2'])
        counter+=1 #same as counter = counter + 1

#2 dictionaries that we'll use for searching fashionnova
#both dictionaries have different formatting. both formats are OK
#1 dictionary has good qualities
#1 dictionary has the qualities of a loser
positive = {
    'strong',
    'independent',
    'athletic',
    'sassy',
    'work'
}

negative = {'excuses','lazy','blame'}

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