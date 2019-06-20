from http.client import HTTPConnection

# www.example.com = 통신 테스트 가능한 기본 사이트
conn = HTTPConnection('www.example.com')

# [REST 형식의 통신 테스트]
# 1. 성공
# GET / HTTP/1.1
conn.request('GET','/')
resp = conn.getresponse()
print(resp.status, resp.reason)

if resp.status == 200:
    body = resp.read()
    print(body)

# 2. 실패(404)
# GET /hello.html HTTP/1.1
conn.request('GET','/hello.html')
resp = conn.getresponse()
print(resp.status, resp.reason)

if resp.status == 200:
    body = resp.read()
    print(body)