from bottle import *
from time import sleep

app=Bottle()
@app.route('/index/<name:re:[0-9]*>')
def index(name='world'):
    #return '<strong>hello {}!'.format(name)
    return template('form.html')

@app.get('/login')
def login_form():
    return template('form.html')

@app.post('/login')
def login():
    name=request.forms.get('name')
    password=request.forms.get('password')
    if name=='admin' and password=='pwd':
        return '<h1>successful!</h1>'
    else:
        #return '<p>sorry!</p>'
        #return template('form.html')
        #redirect('/login')
        abort(404)

@app.route('/static/<filename:path>')
def server_static(filename):
    return static_file(filename,root='/ftp')

@app.error(404)
def error404(error):
    redirect('/hello')


@app.route('/hello')
def hello():
    if request.get_cookie('visited'):
        return 'welcome back! nice to see you again!'
    else:
        response.set_cookie('visited','yes')
        return 'hello there! nice to meet you!'

run(app,host='localhost',port=8080)   #启动本地服务器,host='0.0.0.0'表示让服务器接受所有地址的请求