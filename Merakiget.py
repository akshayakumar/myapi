#!/usr/bin/python
import json
import requests
import mysql.connector
import datetime
conn = mysql.connector.connect(host='127.0.0.1', user='root', password='password', database='Meraki')
c = conn.cursor()
url = "https://n67.meraki.com/api/v0/organizations/191019/networks"

headers = {
    'content-type': "application/json",
    'x-cisco-meraki-api-key': "25350e0d351caa70d3e40fee0ce6e9d8b15998ee",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, headers=headers)

s = json.loads(response.text)



for network in s:
    ##write to mysql
    time = datetime.datetime.now()
    print time
    print network ['name']
    print network['id'] + '\n'
    c.execute("""
        INSERT into network(time, id, name)
        VALUES
            (%s, %s, %s)
        """, (time, network['id'], network['name']))
    conn.commit()
    
    
conn.close()

        


    