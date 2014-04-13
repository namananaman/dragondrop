from flask import Flask, render_template, request
from pymongo import MongoClient




#client = MongoClient()

#db = client.Sessions

app = Flask(__name__)




# Route functions

@app.route('/', methods=['GET', 'POST'])
def index():
	#On a GET request bring them to the index, on a POST request create a session, put it in the db, and redirect the URL
	if request.method == 'GET':
		return render_home()
	else:
		return new_session()

@app.route('/player/<id>')
def player_session(id):
	#given an id, return the session
	#return render_player_session(id)
	return render_home()

@app.route('/DM/<id>')
def DM_session(id):
	#return render_DM_session(id)
	return render_home()
# Template functions

def render_home():
	"""
	Function for rendering the home page
	"""
	return render_template("index.html")

def render_player_session(id):
	"""
	Function for rendering an existing session page
	"""
	sess = get_player_session(id)
	if sess:
		pass
		#return render_template("session.html")
	else:
		pass		
		#some kind of 404

def render_DM_session(id):
	"""
	Function for rendering a DM session page
	"""
	sess = get_DM_session(id)
	if sess:
		pass
	else:
		pass

# Database functions

def new_session():
	pass

def get_player_session(id):
	pass

def get_DM_session(id):
	pass


# Main function

if __name__ == '__main__':
	app.debug = True
	app.run(host='0.0.0.0')
