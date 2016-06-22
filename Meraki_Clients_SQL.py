#!/usr/bin/python
import json
import requests
import mysql.connector
import datetime
conn = mysql.connector.connect(host='127.0.0.1', user='root', password='password', database='Meraki')
c = conn.cursor()
url = "https://n67.meraki.com/api/v0/devices/Q2BN-CNZX-RLTY/clients?timespan=36000"
querystring = {"timespan":"36000"}
headers = {
    'content-type': "application/json",
    'x-cisco-meraki-api-key': "25350e0d351caa70d3e40fee0ce6e9d8b15998ee",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers, params=querystring)
s = json.loads(response.text)

for client in s:
    ##write to mysql
    data = client['usage']
    string =  "Clientname" + " " +client['description'] + " " + "ClientId" + client['id'] +" "+ "SentData" + str(data['sent']) +" "+"RecvData"+str(data['recv']) 
    print string

    c.execute("""
        INSERT into client(name, id, DatasentKb, DatarecvKb)
        VALUES
            (%s, %s, %s, %s)
        """, (client['description'], client['id'], data['sent'], data['recv']))
    conn.commit()
    
conn.close()
