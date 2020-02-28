# _*_ coding utf-8 _*_
# Author: RXC
# Date: 2020/2/288:39
# Filename: server

#请求信息位于environ中，HTTP响应通过start_response()返回头，通过application返回Body

from wsgiref.simple_server import make_server

from hello import application

httpd = make_server('',8000,application)
print('Serving HTTP on port 8000...')
httpd.serve_forever()