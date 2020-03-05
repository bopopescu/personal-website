from flask import Flask, request, redirect, session, render_template, make_response, send_from_directory
from flask_mobility import Mobility
from flask_mobility.decorators import mobile_template
import os


app = Flask(__name__)
app.config.from_pyfile('settings.cfg')
Mobility(app)
# app.config['SECRET_KEY']=b'secretpassword!'
# app.config.from_object('yourapplication.default_settings')
# app.config.from_envvar('YOURAPPLICATION_SETTINGS')





@app.route('/favicon.ico')
def favicon():
    return send_from_directory(os.path.join(app.root_path, 'static'),
                               'favicon.ico', mimetype='image/vnd.microsoft.icon')    
        
@app.route("/")
@mobile_template("{mobile/}home.html")
def home(template):
    return render_template(template)

@app.route("/cv")
@mobile_template("{mobile/}cv.html")
def about(template):
    return render_template(template)

@app.route("/projects")
@mobile_template("{mobile/}projects.html")
def method(template):
    return render_template(template)

@app.route("/contact")
@mobile_template("{mobile/}contact.html")
def results(template):
    return render_template(template)

    
if __name__ == "__main__":
    app.run(threaded=True, host='0.0.0.0')
