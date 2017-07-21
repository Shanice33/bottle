from bottle import *
from bottle_sqlite import SQLitePlugin
install(SQLitePlugin(dbfile='/tmp/test.db'))

app=Bottle()
@app.route('/index/<name:re:[0-9]*>')
def index(name='world'):
    #return '<strong>hello {}!'.format(name)
    return template('form.html')

@app.get('/login')
def login_form():
    return template('form')

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

@error(404)
def error404(error):
    redirect('/ss')
    #return template('form_in.html')
    #return 'error'


@app.route('/hello')
@app.route('/hello/<name>')
@view('h')
def hello(name='world'):
    # if request.get_cookie('visited'):
    #     return 'welcome back! nice to see you again!'
    # else:
    #     response.set_cookie('visited','yes')
    #     return 'hello there! nice to meet you!'
    return dict(name=name)
    #return template('h',name=name)

@app.route('/ss')
def coueter():
    response.set_cookie('counter','4')
    return '{}'.format(request.get_cookie('counter'))

@app.route('/fupload')
def file_upload():
    return template('form_in.html')
@app.route('/upload',method='post')
def do_upload():
    template('form_in.html')
    category=request.forms.get('category')
    upload =request.files.get('upload')
    print(upload)
    if category and upload.file:
        raw = upload.file.read()  # 当文件很大时，这个操作将十分危险
        filename = upload.filename
        return "Hello {}! You uploaded {} ({} bytes).".format(category, filename, len(raw))
    return "You missed a field"


run(app,host='localhost',port=8080)   #启动本地服务器,host='0.0.0.0'表示让服务器接受所有地址的请求