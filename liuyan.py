from flask import *
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os

app=Flask(__name__)
app.secret_key='hello'

conn = sqlite3.connect('user.db')
curr = conn.cursor()
curr.execute("DROP TABLE IF EXISTS user")
curr.execute("CREATE TABLE IF NOT EXISTS user(id INTEGER PRIMARY KEY AUTOINCREMENT ,name VARCHAR(20) UNIQUE NOT NULL ,pwd VARCHAR(20) NOT NULL )")
curr.execute("INSERT INTO user(name,pwd) VALUES (?,?)", ('ss', '33'))
conn.close()
@app.route('/')
def index():
    img=url_for('static',filename='33.jpg')
    username=request.form.get('username','')
    return render_template('hello.html',img=img,name=username)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html')
    else:
        username=request.form.get('username','')
        password=request.form.get('password','')
        print(username,password)
        curr.execute("select * from user WHERE name==? and pwd==?",(username,password))
        data=curr.fetchall()
        if data:
            print(data)
            flash('hello,%s'%username)
            return redirect('/main')
        else:
            flash('ss')
            return redirect('/login')

@app.route('/reg',methods=['GET','POST'])
def regist():
    if  request.method=='GET':
        return render_template('registe.html')
    else:
        username=request.form.get('username','')
        password=request.form.get('password','')
        try:
            curr.execute("INSERT into user(name,pwd) VALUES ('%s','%s')"%(username,password))
            flash("user {} registe ok!".format(username))
            return redirect(url_for('index'))
        except:
            flash('注册失败，请重新注册')
            return redirect(url_for('regist'))

@app.route('/main',methods=['GET','POST'])
def mainpage():
    if request.method=='GET':
        return render_template('mainpage.html',username=request.form.get('username'))
    else:
        name=request.form.get('name','')
        content=request.form.get('content','')
        file=request.files.get('file','')
        if file:
            fname,ext=os.path.splitext(file.filename)
            file.filename=''.join(('123',ext))
            file.save('/static',overwrite=True)
            img=url_for('/static',filename=file.filename)
        return render_template('mainpage.html',name=name,content=content,img=img)

app.run(host='',port=5000,debug=True)