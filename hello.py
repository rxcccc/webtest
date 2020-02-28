# _*_ coding utf-8 _*_
# Author: RXC
# Date: 2020/2/288:37
# Filename: hello

def application (environ , start_responese):
    start_responese('200 ok',[('Content-Type','text/html')])
    body = '<h1>Hello , {}!</h1>'.format(environ['PATH_INFO'][1:]or 'web!')
    return [body.encode('utf-8')]