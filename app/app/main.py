from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def signin():
    return render_template('signin.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/student')
def student():
    return render_template('student.html')

@app.route('/company')
def company():
    return render_template('company.html')

@app.route('/mentor')
def mentor():
    return render_template('mentor.html')

@app.route('/institution')
def institution():
    return render_template('institution.html')

if __name__ == '__main__':
    app.run(debug=True)
