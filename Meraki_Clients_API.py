#!/usr/bin/python
import json
import requests
import mysql.connector
import datetime

url = "https://n67.meraki.com/api/v0/devices/Q2BN-CNZX-RLTY/clients?timespan=36000"
querystring = {"timespan":"36000"}
headers = {
    'content-type': "application/json",
    'x-cisco-meraki-api-key': "",
    'cache-control': "no-cache"
    }

sparkurl = "https://api.ciscospark.com/v1/webhooks/incoming/"

sparkheader = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer ",
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
    payload = { 'roomId': "",
               'text': string}
    spark = requests.request("POST", sparkurl, data=json.dumps(payload), headers=sparkheader)
