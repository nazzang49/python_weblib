from http.server import BaseHTTPRequestHandler, HTTPServer
from urllib.parse import urlparse, parse_qs

port = 9999

# BaseHTTPRequestHandler 상속
class SimpleHTTPRequestHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        print(self.path)
        # if '?' in self.path:
        #     # path 와 parameter 정보 구분
        #     urls = self.path.split('?')
        #     path = urls[0]
        #     # parameter 정보 구분(파라미터1, 파라미터2, etc)
        #     qs = urls[1].split('&')
        #     print(path, qs)

        result = urlparse(self.path)
        params = parse_qs(result.query)
        print(params)

        # 요청에 대한 응답
        self.send_response(200)
        self.send_header('Content-Type','text/html; charset=utf-8')
        self.end_headers()
        self.wfile.write('<h1>하이</h1>'.encode('utf-8'))

# 서버 객체 생성
httpd = HTTPServer(('0.0.0.0',port),SimpleHTTPRequestHandler)
print(f'<< server is running now on {port} >>')
httpd.serve_forever()