#Challenge 2: Reverses a given string
import urllib2
import json
import requests

#token dictionary
myTokenDic = {'token': 'dd37a340075703941693f52801282791'}
#request the word
getIt = requests.post('http://challenge.code2040.org/api/reverse', json = myTokenDic)
#turn the word into text
wordText = getIt.text
#reverse the word
reverse = wordText[::-1]
#JSon Dictionary
jsonDic={'token': 'dd37a340075703941693f52801282791', 'string': reverse}
#post the JSon Dictionary to the site
postIt = requests.post('http://challenge.code2040.org/api/reverse/validate', json=jsonDic)

