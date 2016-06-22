#!/usr/bin/python
import json
import requests
import mysql.connector
import datetime

url = "https://n67.meraki.com/api/v0/organizations/191019/networks"

headers = {
    'content-type': "application/json",
    'x-cisco-meraki-api-key': "25350e0d351caa70d3e40fee0ce6e9d8b15998ee",
    'cache-control': "no-cache"
    }

sparkurl = "https://api.ciscospark.com/v1/messages"

sparkheader = {
    'content-type': "application/json; charset=utf-8",
    'authorization': "Bearer YzRhNmU1YmUtOGQ5NC00NjcxLTllYWYtNjAzMzVhODg2NjE0NTAxY2ViY2UtMmJm",
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
    payload = { 'roomId': "Y2lzY29zcGFyazovL3VzL1JPT00vMWFlYzE5NDAtMzdmMy0xMWU2LWFjZGQtNDk0YjNhOWJlOWY1",
               'text': string}
    spark = requests.request("POST", sparkurl, data=json.dumps(payload), headers=sparkheader)