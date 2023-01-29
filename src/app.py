from flask import Flask, jsonify, render_template
import platform
import socket

app = Flask(__name__)

def myHost():
    hostname = platform.node()
    #s = socket.gethostname()
    ip = socket.gethostbyname(hostname)
    return str(hostname), str(ip)

@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route('/health')
def health():
    return jsonify(
        status = "up"
    )

@app.route('/details')
def details():
    hostname, ip = myHost()
    return render_template('index.html', HOSTNAME=hostname, IP=ip)



#change port to whichever...
if __name__ == '__main__':
    app.run(host = '0.0.0.0', port=80)