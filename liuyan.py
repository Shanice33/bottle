from flask import *
from flask_sqlalchemy import SQLAlchemy
import sqlite3
import os
import datetime

app=Flask(__name__)
app.secret_key='hello'

conn = sqlite3.connect('use.db')
curr = conn.cursor()
curr.execute("DROP TABLE IF EXISTS use")
curr.execute("DROP TABLE IF EXISTS message")
curr.execute("CREATE TABLE IF NOT EXISTS use(id INTEGER PRIMARY KEY AUTOINCREMENT ,name VARCHAR(20) UNIQUE NOT NULL ,pwd VARCHAR(20) NOT NULL)")
curr.execute("CREATE TABLE IF NOT EXISTS message(id INTEGER PRIMARY KEY AUTOINCREMENT ,name VARCHAR(20)  ,word varchar(1000),time_at datetime,filename varchar(50))")
#curr.execute("INSERT INTO use(name,pwd) VALUES (?,?)", ('ss', '33'))
curr.close()
conn.close()

@app.route('/')
@app.route('/?name=<name>')
def index(name=None):
    img=url_for('static',filename='33.jpg')
    return render_template('hello.html',img=img,name=name)

@app.route('/login',methods=['GET','POST'])
def login():
    if request.method=='GET':
        return render_template('login.html',name=request.form.get('username',''))
    else:
        username=request.form.get('username','')
        password=request.form.get('password','')
        conn = sqlite3.connect('use.db')
        curr = conn.cursor()
        curr.execute("select * from use WHERE name==? and pwd==?",(username,password))
        data=curr.fetchall()
        curr.close()
        conn.close()
        if data:
            #flash('hello,%s'%username)
            return redirect(url_for('mainpage',name=username))
        else:
            flash('登陆失败,该用户不存在或密码错误')
            return redirect('/login')

@app.route('/reg',methods=['GET','POST'])
def regist():
    if  request.method=='GET':
        return render_template('registe.html')
    else:
        username=request.form.get('username','')
        password=request.form.get('password','')
        try:
            conn = sqlite3.connect('use.db')
            curr=conn.cursor()
            curr.execute("INSERT into use( name,pwd) VALUES ('%s','%s')"%(username,password))
            conn.commit()
            curr.execute("select * from use")
            data = curr.fetchall()
            print(data)
            flash("user {} registe ok!".format(username))
            curr.close()
            conn.close()
            return redirect(url_for('index',name=username))
        except:
            flash('注册失败,该用户名已存在，请重新注册')
            return redirect(url_for('regist'))

@app.route('/main',methods=['GET','POST'])
@app.route('/main?name=<name>',methods=['GET','POST'])
def mainpage(name=None):
    if request.method=='GET':
        return render_template('mainpage.html',username=name)
    else:
        conn = sqlite3.connect('use.db')
        curr = conn.cursor()
        username=request.form.get('name','')
        content=request.form.get('content','')
        now = datetime.datetime.now()
        now = now.strftime('%Y-%m-%d %H:%M:%S')
        file=request.files.get('file','')
        if file:
            file.save(os.path.join('static',file.filename))
        curr.execute("INSERT into message( name,word,time_at,filename) VALUES (?,?,?,?)",(username, content, now,file.filename))
        conn.commit()
        curr.execute("select * from message")
        data = curr.fetchall()
        print(data)
        curr.close()
        conn.close()
        return redirect('/view')

@app.route('/view')
def view():
    conn = sqlite3.connect('use.db')
    curr = conn.cursor()
    curr.execute('select name,word,time_at,filename from message')
    mess = curr.fetchall()
    print(mess)
    curr.close()
    conn.close()
    # for item in mess:
    #     f = url_for('static', filename=item[3])
    return render_template('view.html',mess=mess)

app.run(host='',port=5000,debug=True)