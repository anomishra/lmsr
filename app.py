from flask import Flask, render_template, request, make_response, jsonify
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
	investor_count = request.args.get('investor_count')
	print(investor_count)

	if investor_count == None:
		investor_count = 10
	else:
		investor_count = int(investor_count)

	b_number = request.args.get('b_number')
	if b_number == None:
		b_number = 500
	else:
		b_number = int(b_number)

	budget = request.args.get('budget')
	if budget == None:
		budget = 500
	else:
		budget = int(budget)

	print(investor_count)
	return LMRS.init(investor_count, b_number, budget)

@app.route('/lmrs/info', methods=['GET'])
def get_market_info():
	return jsonify(LMRS.gen_market_info())


@app.route('/lmrs/next_day', methods=['GET'])
def run_for_next_day():
	return jsonify(LMRS.run_for_next_day())


if __name__ == '__main__':
	app.run( host="0.0.0.0",	 port=int("8080")	 )
