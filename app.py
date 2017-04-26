from flask import Flask, render_template, request

import logging

logger = logging.getLogger(__name__)


#######################
#### configuration ####
#######################

app = Flask(__name__, static_folder='static', static_url_path='')
# app.config.from_object(os.environ['APP_SETTINGS'])


################
#### routes ####
################
@app.route('/index', methods=['GET'])
def index():
	return 'nothing!!'


if __name__ == '__main__':
	app.run( host="0.0.0.0",	 port=int("8080")	 )
