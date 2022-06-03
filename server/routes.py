from flask import Flask, redirect, render_template, url_for
from flask_socketio import SocketIO, send, emit
import socketio

# Login
from forms import LoginForm

# Configure app
app = Flask(__name__)
app.config['SECRET_KEY'] = "jfl;akjfa;"
socketio = SocketIO(app)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        return redirect(url_for("index"))

    return render_template("login.html", form=form)

@socketio.on("message")
def handle_message(msg):
   send(msg, callback=ack)

def ack():
    print('message was received!')

if __name__ == "__main__":
    socketio.run(app, debug=True, port=3000)