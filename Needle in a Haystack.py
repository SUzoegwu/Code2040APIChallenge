#Challenge 3: Find the index of the needle in an array of list
import urllib2
import json
import requests


#token dictionary
myTokenDic = {'token': 'dd37a340075703941693f52801282791'}
#request the word
getIt = requests.post('http://challenge.code2040.org/api/haystack', json = myTokenDic)
#convert from response object to a python object
pythonObject = getIt.json()
#counter to see where value is
counter = int (0)
#iterate through the haystack list and find which index is the needle
for i in range (0, (len(pythonObject['haystack'])-1)):
    if (pythonObject['needle']==pythonObject['haystack'][i]):
        counter = i
        break

#JSon Dictionary
jsonDic={'token': 'dd37a340075703941693f52801282791', 'needle': counter}
#post the JSon Dictionary to the site
postIt = requests.post('http://challenge.code2040.org/api/haystack/validate', json=jsonDic)
