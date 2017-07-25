import urllib.parse,urllib.request

print(urllib.parse.urlparse('http://www.baidu.com'))
#print(urllib.request.urlopen('http://www.baidu.com').info())
print(urllib.request.urlretrieve('http://www.baidu.com')[0])  #返回二元组(filename,web服务器响应后返回的一系列MIME文件头))
