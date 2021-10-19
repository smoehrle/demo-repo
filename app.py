from flask import Flask
import time
import urllib.request

app = Flask(__name__)

@app.route("/")
def hello_world():
    time.sleep(25)
    instanceid = urllib.request.urlopen('http://169.254.169.254/latest/meta-data/instance-id').read().decode()
    return f"<p>Hello, World! I'm {instanceid}</p>"


@app.route("/health")
def health():
    return "Healthy"