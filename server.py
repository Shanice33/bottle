from wsgiref.simple_server import make_server
from hello import application

#创建一个服务器，可以接受任何ip地址的主机，端口是8000，处理函数是application
httpd=make_server('',8000,application)
print('serving http on port 8000..')
#开始监听http请求
httpd.serve_forever()