import requests

endpoint="https://github.com"
endpoint2="https://httpbin.org/anything"
endpoint3="https://gl-tbf.org/"
endpoint4="http://127.0.0.1:8000/api/products/1/update/"

data={
  "title":"Xp",
  "body":"Hieee"
 }


gr_=requests.put(endpoint4,json=data)
print(gr_.json())
