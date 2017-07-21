from bottle import *

@route('/login')
def login_form():
    return  template('form.html')

@post('/login')
def login():
    name=request.forms('name')
    pwd=request.forms('password')
    if name=='admin' and pwd=='pwd':
        return 'hello'
    else:
        abort(404)
@route('/hello')
def hello():
    return "hello"

@error(404)
def error404(error):
    redirect('/hello')



run('',8080)