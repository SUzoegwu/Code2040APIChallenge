#Challenge 5: Updates date times with a given interval
import urllib2
import json
import requests


#token dictionary
myTokenDic = {'token': 'dd37a340075703941693f52801282791'}
#request the word
getIt = requests.post('http://challenge.code2040.org/api/dating', json = myTokenDic)
#convert from response object to a python object
print getIt.text
pythonObject = getIt.json()

#parsed the datestamp into separate categories, day, month, year, etc
day = int(pythonObject['datestamp'][8:10])
year = int(pythonObject['datestamp'][0:4])
month = int(pythonObject['datestamp'][5:7])
hours = int(pythonObject['datestamp'][11:13])
mins = int(pythonObject['datestamp'][14:16])
secs = int(pythonObject['datestamp'][17:19])
theInterval = int(pythonObject['interval'])

#set the changes in scenarios when the numbers are too big for the previous category
#the Seconds deal with all numbers less than 60
theSeconds = theInterval % 60
#the mins with all numbers greater than 60
theMins = theInterval / 60
theHours = int (0)
theDay = int (0)
theMonth = int (0)
theYear = int (0)

#if seconds is outside boundary, update the minutes
if((theSeconds + secs) > 60):
    theMins = theMins + 1
    secs = theSeconds +secs - 60
else:
    secs = theSeconds + secs

#if minutes is outside boundary, update the hours
if((theMins + mins) > 60):
    theHours = (theMins+mins) / 60
    mins = (theMins +mins)%60
else:
    mins = theMins + mins

#if hours is outside boundary, update the days    
if((theHours + hours)>24):
    theDay = theDay + (theHours+hours)/24
    hours = (theHours+hours)%24
else:
    hours = hours+theHours

#if days is outside boundary, update the months
if((theDay + day) > 31):
    theMonth = theMonth + (theDay + day)/31
    day = (theDay + day)%31
else:
    day = theDay + day

#if months is outside boundary, update the days
if((theMonth + month)>12):
    theYear = theYear + (theMonth + month)/31
    month = (theMonth + month)%12
else:
    month = theMonth + month

#update the year after everything
year = year+theYear

#if hours is less than 10, adjust the setting and print, else print normally
if(hours<10):
    hours = "0"+str(hours)
    returnString=str(year)+"-"+str(month)+"-"+str(day)+"T"+hours+":"+str(mins)+":"+str(secs)+"Z"
else:
    returnString=str(year)+"-"+str(month)+"-"+str(day)+"T"+str(hours)+":"+str(mins)+":"+str(secs)+"Z"



#JSon Dictionary
jsonDic={'token': 'dd37a340075703941693f52801282791', 'datestamp': returnString}
#post the JSon Dictionary to the site
postIt = requests.post('http://challenge.code2040.org/api/dating/validate', json=jsonDic)
print postIt.text
