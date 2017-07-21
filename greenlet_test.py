from gevent import monkey;monkey.patch_all()
from time import  sleep
from bottle import route,run

@route('/stream')
def stream():
    yield 'start'
    sleep(3)
    yield 'middle'
    sleep(5)
    yield 'end'

run(host='0.0.0.0',port=8000)
