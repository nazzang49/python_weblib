from urllib.parse import urlparse

# 흔히 생략하는 full url pattern
result = urlparse('http://www.python.org:80/guido/python.html;philosophy?overall=3#here')
print(result)