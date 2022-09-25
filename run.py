import time, logging

from cfg       import *
from flask     import Flask, request, render_template, abort
from datetime  import datetime

app = Flask(__name__)



# Routes
@app.route('/')
def index():
    return render_template('index.html')

# This will run before each request
@app.before_request
def before_request_func():
    if PROXY:
        value_ip   = request.environ.get('HTTP_X_REAL_IP')
    else:
        value_ip   = request.environ.get('REMOTE_ADDR')
    # This will block IP if found in block list
    if value_ip in LIST_BLOCK:
        print('Blocked IP:\t' + value_ip)
        abort(403)

    # This will allow IP if found in allow list
    if value_ip in LIST_ALLOW:
        pass
    else:
        print('Not Allowed IP:\t' + value_ip)
        abort(403)

if __name__ == '__main__':
   app.run(host = IP , port = PORT , debug = DEBUG)