#Challenge 4: Removes words with the given prefix from an Array List
import urllib2
import json
import requests


#token dictionary
myTokenDic = {'token': 'dd37a340075703941693f52801282791'}
#request the word
getIt = requests.post('http://challenge.code2040.org/api/prefix', json = myTokenDic)
#convert from response object to a python object
pythonObject = getIt.json()
#counter to see where value is
returnArray = []

#iterate through the array of strings
for i in range (0, (len(pythonObject['array'])-1)):
    #iterate through each string and if it doesnt have the prefix, add to list
    for j in range(0, len(pythonObject['prefix']) -1):
        if (pythonObject['prefix'][j] == pythonObject['array'][i][j]):
            ()
        else:
            returnArray.append(pythonObject['array'][i])
            break

#JSon Dictionary
jsonDic={'token': 'dd37a340075703941693f52801282791', 'array': returnArray}
#post the JSon Dictionary to the site
postIt = requests.post('http://challenge.code2040.org/api/prefix/validate', json=jsonDic)
print postIt.text
