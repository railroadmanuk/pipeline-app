from flask import Flask, render_template
import os
import datetime

app = Flask(__name__)

environment = os.environ["APP_ENVIRONMENT"]
images_path = os.environ["APP_IMAGES_PATH"]
app_version = '0.0.1'
app = Flask(__name__)

@app.route('/')
def index():
    time_now = datetime.datetime.now().isoformat()
    return render_template( 'index.html', timeNow = time_now, app_version = app_version )
    #return ('This is the '+environment+' environment. Hello, World!')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')