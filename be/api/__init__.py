from flask import Flask

app = Flask(__name__)
app.config["DEBUG"] = True

@app.after_request
def enableCors(response):
	response.headers.add('Access-Control-Allow-Origin', '*')
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PUT,POST,DELETE,OPTIONS')
	return response

import api.services
