def index():
	if request.method == 'GET':
		return render_template('index.html')

@app.route("/login", methods=['GET','POST'])

def login():
	if request.method == 'GET':
		return render_template('login.html')
	elif request.method == 'POST':
		varusername=request.form['eusername']
		varpassword=request.form['epassword']
		profiles = json.load(open('profiles.json'))

		print profiles['profiles']

		for profile in profiles['profiles']:
			print(profile)
			if varusername== "Admin" and varpassword==  'Stanky123':
				return redirect(url_for('show_all'))
			elif profile['cusername'] == varusername and profile['cpassword'] == varpassword:
				return redirect(url_for('getprofile',foruser=profile['cusername']))
		return "Wrong password"

@app.route("/show_all")
def show_all():
	ctable = json.load(open('profiles.json'))

	return render_template('show_all.html',allprofiles=ctable)
