from bottle import *

app=Bottle(__name__)

@app.route('/')
def hello():
    name='jhy'
    content='<h1>hello {}!</h1>'.format(name)
    return  content

messages=[]  #存放提交的表格的内容
@app.route('/message')
@app.post('/message')
def message_view():
    #print('method:',request.method)

    if request.method=='GET':
        name=request.GET.getunicode('name','').strip()
        content=request.GET.get('content','').strip()
        #print(name)
        msg_1={
              'name':name,
              'content':content
          }
        messages.append(msg_1)
        print(messages)

    if request.method=='POST':
        #print('post的表单数据：',request.forms)
        name=request.forms.getunicode('name','').strip()
        content=request.forms.get('content','').strip()
        msg_2={
             'name':name,
             'content':content
         }
        messages.append(msg_2)
        #print(messages)
    return template('msg',msgs=messages)

if __name__=='__main__':
    debug=True
    app.run(host='0.0.0.0',port=8080,debug=debug)

