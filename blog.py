from bottle import *
import os,sqlite3

app=Bottle()

#app_list={'js':'ss','jhy':'ss'}
conn=sqlite3.connect('user.db')
curr=conn.cursor()
curr.execute("DROP TABLE IF EXISTS user")
curr.execute("create table IF NOT EXISTS user(id integer PRIMARY KEY AUTOINCREMENT ,name varchar(20),pwd VARCHAR(20))")
curr.execute("INSERT into user(name,pwd) VALUES (?,?)",('ss','33'))
curr.execute("INSERT into user(name,pwd) VALUES ('%s','%s')"%('jhy','33'))
#imagepath=os.path.join(os.getcwd(),'33.jpg')
#print(imagepath)

@app.route('/')
def index():
    username=request.GET.get('username','')
    nav_list=['首页','经济','文化','科技','娱乐']
    blog={'title':'welcome to my blog','content':'hello,welcome to my blog'}
    btag={'js':'(10)','python':'(20)','shell':'(5)'}
    img=static_file('33.jpg',root='./')
    return template('index.html',username=username,nav_list=nav_list,blog=blog,blogtag=btag,img=img)

@app.route('/reg',method=['GET','POST'])
def regist():
    if request.method=='GET':
        return template('registe.html')
    else:
        username=request.forms.get('username')
        password=request.forms.get('password')
        curr.execute("insert into user(name,pwd) VALUES ('%s','%s')"%(username,password))
        conn.commit()
        curr.execute("SELECT * from user")
        data = curr.fetchall()
        print(data)
        #app_list[username]=password
        return 'user {} regist ok!'.format(username)

@app.route('/login',method=['GET','POST'])
def login():
    if request.method=='GET':
        return template('login.html')
    else:
        username=request.forms.get('username')
        password=request.forms.get('password')
        # if (username,password) in app_list.items():
        #     #response.set_cookie(value=username,max_age=300)
        #     redirect('/')
        #
        # else:
        #     redirect('/login')
        curr.execute("SELECT * FROM user WHERE name=='%s' and pwd=='%s'"%(username,password))
        data=curr.fetchall()
        if data:
            redirect('/')
        else:
            redirect('/login')

@app.route('/upload',method=['get','post'])
def upload():
    if request.method=='GET':
        return template('upload.html')
    else:
        username=request.forms.get('username')
        file=request.files.get('img')
        name,ext=os.path.splitext(file.filename)
        file.filename=''.join(('123',ext))
        file.save('./',overwrite=True)
        return static_file(file.filename,root='./')



run(app,host='',port=8080)


