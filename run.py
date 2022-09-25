import time, logging

from cfg       import *
from flask     import Flask, request, render_template, g
from datetime  import datetime

app = Flask(__name__)

# This will disable Flask logging when clean logging is enabled
if CLEAN_LOG:
    log = logging.getLogger('werkzeug')
    log.disabled = True

# Routes
@app.route('/')
def index():
    # This simulates a duration for request
    time.sleep(0.1)
    return render_template('index.html')

@app.route('/contact')
def contact():
    # This simulates a duration for request
    time.sleep(0.15)
    return render_template('contact.html')

# This function prints to console
def log_console(ip, time, path, duration):
    print(  '' + ip + '\t' + time + '\t' + duration + '\t' + '' + path)

@app.before_request
def before_request_func():
    g.request_start_time = time.time()

if CLEAN_LOG:
    @app.after_request
    def after_request_func(response):
        duration  = str(time.time() - g.request_start_time)[:5]
        if PROXY:
            val_ip   = request.environ.get('HTTP_X_REAL_IP')
        else:
            val_ip   = request.environ.get('REMOTE_ADDR')
        val_path = request.path
        val_time = str(datetime.now())[:19]
        if HIDE_STATIC:
            if 'static' not in request.path:
                log_console(val_ip, val_time, val_path, duration)
        else:
            log_console(val_ip, val_time, val_path, duration)
        return response

if __name__ == '__main__':
   app.run(host = IP , port = PORT , debug = DEBUG)