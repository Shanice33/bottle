from flask import Flask
from  flask import  request,render_template

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def home():
    #return '<h1>Home</h1>'
    return render_template('home.html')

@app.route('/sign',methods=['GET'])
def sign_form():
    # return '''<form action="/sign" method="post">
    #            <p><input name="username"></p>
    #            <p><input name="pwd" type="password"></p>
    #            <p><button type="submit">Sign In</button></p>
    #            </form>'''
    return  render_template('form.html')

@app.route('/sign',methods=['POST'])
def sign():
    if request.form['username']=='admin' and request.form['pwd']=='pwd':
        return render_template('sign_ok.html',username=request.form['username'])
    return render_template('form.html',message='bad username or password',username=request.form['username'])
    #     return '<h3>hello,admin!</h3>'
    # return '<h3>bad username or password'


if __name__=='__main__':
    app.run()