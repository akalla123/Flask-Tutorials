from flask import Flask, render_template, request
app = Flask(__name__)

@app.route('/')
def index():
	return render_template("2.html")

@app.route('/signup')
def signup():
	return render_template('signup.html')

@app.route('/success', methods=['GET', 'POST'])
def success():
	if request.method == 'POST':
		fname = request.form['fname']
		lname = request.form['lname']
		email = request.form['email']
		password = request.form['pass']
	else:
		return "Error! Page not Found"
	return render_template("success.html", data = [fname])


if __name__ == '__main__':
	app.run(debug=True)