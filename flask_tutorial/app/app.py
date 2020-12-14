import socket
from flask import Flask

app = Flask(__name__)

@app.route('/ping')
def ping():
    return 'PONG UCLM from {}'.format(socket.getfqdn()), 200


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
