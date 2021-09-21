from urllib import request, parse
import json

# GET
req = request.Request("https://httpbin.org/get")
res = request.urlopen(req)

status = res.status
data = json.loads(res.read().decode('utf-8'))

print(status)

print(data)

print(data.get("headers"))

print(data.get("headers").get("Accept-Encoding"))
print(data.get("headers").get("Host"))
print(data.get("headers").get("User-Agent"))
print(data.get("headers").get("X-Amzn-Trace-Id"))


# # POST (JSON)
# headers = {'Content-Type': 'application/json; chearset=utf-8'}
# data = {'title': 'dummy title', 'id': 1, 'message': 'hello world!'}
# req = request.Request('"https://httpbin.org/get" ', headers=headers, data=json.dumps(data).encode('utf-8'))
# res = request.urlopen(req)
# print(str(res.status) + " | " + res.read().decode('utf-8'))