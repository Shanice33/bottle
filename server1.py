import os
import re
import urllib.request
from  bottle import  *
import qrcode

app=Bottle()
@app.route('/')
def hello():
    return 'welcome!'

@app.route('/qr',method='get')
def show():
    name=request.GET.get('s','')
    if not  name:
        return template('templateStr',m='')
    else:
        qrImg='<img src="http://chart.apis.google.com/chart?chs=300x300&cht=qr&choe=UTF-8&chl=' + name + '" /><br />' + urllib.request.unquote(name)
        return template('templateStr',m=qrImg)

@error(404)
def error404(error):
    return 'sorry'+redirect('/')

run(app,host='',port=8080,debug=True)