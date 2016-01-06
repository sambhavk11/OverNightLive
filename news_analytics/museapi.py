import json
import requests

def getDetails(param):
    url = "https://api.musement.com"+param
    print (url)
    payload = {
      "apikey": "78d01615d38f506c3f10b2d9e1f5b219",
      "Content-Type": "application/json",
      "count": "25",
      "outputMode": "json",
      "cache-control":"no-cache",
    }
    res = requests.get(url,params=payload)
#    jres=res.text
#   return jres

    with open("dummy.json", 'w') as f:
         f.write(res.text)


#getNews("/api/v3/categories")
