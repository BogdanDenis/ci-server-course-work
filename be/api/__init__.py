from flask import Flask, request

app = Flask(__name__)
app.config["DEBUG"] = True

@app.after_request
def enableCors(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response

def shutdown_server():
	func = request.environ.get('werkzeug.server.shutdown')
	if func is None:
		raise RuntimeError('Not running with the Werkzeug Server')
	func()

@app.route('/__kill__', methods=['POST'])
def shutdown():
	shutdown_server()
	return 'Server shutting down...'

import api.services
