from urllib.parse import urlencode
from urllib.request import urlopen, Request

# urlopen은 HTTPResponse 타입의
# get 방식은 주소줄에 파라미터로 전달
response = urlopen('http://www.naver.com?a=100')
body = response.read()
print(body.decode('utf-8'))

# post (별도의 데이터 형성 후 인자로 젼달)
# 1. 요청 데이터 작성
data = {
    'email':'nazzang49@naver.com',
    'password':'1234',
    'name':'박진영'
}
# 2. 요청 데이터 인코딩
data = urlencode(data).encode('utf-8')

# 3. 요청 객체 생성
request = Request('http://www.example.com',data)
request.add_header('Content-Type', 'text/html')

# 4. urlopen을 통해 요청 객체 전송 = 응답 객체
response = urlopen(request)

# 5. 응답 객체 디코딩
print(response.read().decode('utf-8'))








