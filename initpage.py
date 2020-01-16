from flask import Flask , render_template 
app = Flask(__name__)


posts = [
	{
	'author': 'Dimit Drag',
	'content': 'First tweet',
	'date_posted': '07/11/18'
	},
	{
	'author': 'Eleonora Malkova',
	'content': 'Second tweet',
	'date_posted': '08/11/18'
	}
]

@app.route('/')
def index():
        return render_template('loginpage.html'), 200

@app.route('/homepage/')
def hopepage():
	return render_template('screenpage.html', posts=posts), 200

@app.route('/pictures/')
def pictures():
        return render_template('baselayout.html'), 200

@app.route('/profile/')
def profile():
        return render_template('profilepage.html'), 200

@app.route('/register/')
def register():
        return render_template('registerpage.html'), 200

if __name__ == "__main__":
	app.run(host='0.0.0.0', debug=True)
