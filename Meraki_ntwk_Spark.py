#!/usr/bin/python
import json
import requests
import mysql.connector
import datetime

url = "https://n67.meraki.com/api/v0/organizations/191019/networks"

headers = {
    'content-type': "application/json",
    'x-cisco-meraki-api-key': "",
    'cache-control': "no-cache"
    }

sparkurl = "https://api.ciscospark.com/v1/messages"

sparkheader = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer ",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

s = json.loads(response.text)

for network in s:
    ##write to mysql
    time = datetime.datetime.now()
    string = str(time) + network ['name'] + network['id'] 
    print time
    print network ['name']
    print network['id'] + '\n'
    payload = { 'roomId': "",
               'text': string}
    spark = requests.request("POST", sparkurl, data=json.dumps(payload), headers=sparkheader)
