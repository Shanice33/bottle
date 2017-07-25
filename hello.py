def application(environ,start_response):
    start_response('200 OK',[('Content-type','text/html')])
    print(environ.items())
    body='hello %s'%(environ['PATH_INFO'][1:] or 'web')
    return [body.encode('utf-8')]