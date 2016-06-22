#!/usr/bin/python
import json
import requests
import mysql.connector
import datetime

neturl = "https://n67.meraki.com/api/v0/organizations/191019/networks"

netheaders = {
    'content-type': "application/json",
    'x-cisco-meraki-api-key': "25350e0d351caa70d3e40fee0ce6e9d8b15998ee",
    'cache-control': "no-cache"
    }

#URL for Chitti Bot
sparkurl = "https://api.ciscospark.com/v1/webhooks/incoming/Y2lzY29zcGFyazovL3VzL1dFQkhPT0svZjEzNjM2NDQtYTk5YS00MjdkLWI4YWYtNzhhODk5MThlYWI4"

sparkheader = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer YzRhNmU1YmUtOGQ5NC00NjcxLTllYWYtNjAzMzVhODg2NjE0NTAxY2ViY2UtMmJm",
    'cache-control': "no-cache"
    }

response = requests.request("GET", neturl, headers=netheaders)

s = json.loads(response.text)

for network in s:
    ##write to mysql
    time = datetime.datetime.now()
    string = str(time) + network ['name'] + network['id'] 
    print time
    print network ['name']
    print network['id'] + '\n'
    payload = { 'roomId': "Y2lzY29zcGFyazovL3VzL1JPT00vMWFlYzE5NDAtMzdmMy0xMWU2LWFjZGQtNDk0YjNhOWJlOWY1",
               'text': string}
    spark = requests.request("POST", sparkurl, data=json.dumps(payload), headers=sparkheader)
    

url = "https://n67.meraki.com/api/v0/devices/Q2BN-CNZX-RLTY/clients?timespan=36000"
querystring = {"timespan":"36000"}
headers = {
    'content-type': "application/json",
    'x-cisco-meraki-api-key': "25350e0d351caa70d3e40fee0ce6e9d8b15998ee",
    'cache-control': "no-cache"
    }

sparkurl = "https://api.ciscospark.com/v1/webhooks/incoming/Y2lzY29zcGFyazovL3VzL1dFQkhPT0svZjEzNjM2NDQtYTk5YS00MjdkLWI4YWYtNzhhODk5MThlYWI4"

sparkheader = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer YzRhNmU1YmUtOGQ5NC00NjcxLTllYWYtNjAzMzVhODg2NjE0NTAxY2ViY2UtMmJm",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)

s = json.loads(response.text)

for client in s:
    ##write to mysql
    time = datetime.datetime.now()
    data = client['usage']
    string = str(time) + " " + "Clientname" + " " +client['description'] + " " + "ClientId" + client['id'] +" "+ "SentData" + str(data['sent']) +" "+"RecvData"+str(data['recv']) 
    print time
    print  client['description']
    print str(data['sent']) + '\n'
    print str(data['recv']) + '\n'
    payload = { 'roomId': "Y2lzY29zcGFyazovL3VzL1JPT00vMWFlYzE5NDAtMzdmMy0xMWU2LWFjZGQtNDk0YjNhOWJlOWY1",
               'text': string}
    spark = requests.request("POST", sparkurl, data=json.dumps(payload), headers=sparkheader)