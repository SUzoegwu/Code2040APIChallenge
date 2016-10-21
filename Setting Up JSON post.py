#Challenge 1: Set up a JSON post
import urllib2
import json
import requests

#JSon Dictionary
jsonDic={'token': 'dd37a340075703941693f52801282791', 'github': 'https://github.com/SUzoegwu/Code2040APIChallenge'}
#request access to the register
r = requests.get('http://challenge.code2040.org/api/register')
#post the JSon Dictionary to the site
r = requests.post('http://challenge.code2040.org/api/register', json=jsonDic)


