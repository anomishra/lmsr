from flask import Flask, render_template, request, make_response
from flask_cors import CORS, cross_origin

from functools import wraps, update_wrapper
from datetime import datetime
from lmrs import LMRS
import logging

logger = logging.getLogger(__name__)


def nocache(view):
	@wraps(view)
	def no_cache(*args, **kwargs):
		response = make_response(view(*args, **kwargs))
		response.headers['Last-Modified'] = datetime.now()
		response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
		response.headers['Pragma'] = 'no-cache'
		response.headers['Expires'] = '-1'
		print('asasas')
		return response

	return update_wrapper(no_cache, view)

#######################
#### configuration ####
#######################

app = Flask(__name__, static_folder='static', static_url_path='')

CORS(app)


################
#### routes ####
################
@app.route('/index', methods=['GET'])
@nocache
def index():
	return render_template('index.html')


@app.route('/lmrs/init', methods=['GET'])
def init_lmrs():
	return LMRS.init()

if __name__ == '__main__':
	app.run( host="0.0.0.0",	 port=int("8080")	 )
