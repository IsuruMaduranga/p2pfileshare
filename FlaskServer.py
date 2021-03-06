import threading
import sys
import logging
from flask import Flask, Response, request, send_file

cli = sys.modules['flask.cli']
cli.show_server_banner = lambda *x: None
log = logging.getLogger('werkzeug')
log.setLevel(logging.ERROR)

class EndpointAction(object):
   def __call__(self, file):
      return send_file(file)

class FlaskServer(object):
	app = None
	
	def __init__(self, name):
		self.app = Flask(name)

	def run(self):
		threading.Thread(target=self.app.run).start()
	
	def add_endpoint(self, endpoint=None, endpoint_name=None):
		self.app.add_url_rule(endpoint, endpoint_name, EndpointAction())