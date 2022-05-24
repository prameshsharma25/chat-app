from flask import Flask, render_template
from flask_socketio import SocketIO, send, emit
import socketio

app = Flask(__name__)
app.config['SECRET_KEY'] = ""
socketio = SocketIO(app)

@app.route("/login")
def login():
    return render_template("login.html")

@socketio.on("message")
def handle_message(msg):
   send(msg, callback=ack)

def ack():
    print('message was received!')

if __name__ == "__main__":
    socketio.run(app, debug=True, port=3000)