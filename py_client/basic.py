import requests

endpoint="https://github.com"
endpoint2="https://httpbin.org/anything"
endpoint3="https://gl-tbf.org/"
endpoint4="http://127.0.0.1:8000/api/products"


#gr_=requests.get(endpoint4,json={"query":"Hello"},params={"abc":123})
gr_=requests.get(endpoint4)
print(gr_.json())
