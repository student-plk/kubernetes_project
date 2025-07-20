from flask import Flask
import socket

app=Flask(__name__)


@app.route("/home")
def myhome():
	hostname = socket.gethostname()
	IPaddr = socket.gethostname(hostname)
	return f"Welcome to Palak Saini's page....<br> my hostname:{hostname} <br> myIP:{IPAddr}"

app.run(host="0.0.0.0")