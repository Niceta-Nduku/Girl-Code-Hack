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

@app.route('/home')
def home():
    return render_template('home.html')

@app.route('/compHome')
def compHome():
    return render_template('compHome.html')

@app.route('/MentorHome')
def MentorHome():
    return render_template('MentorHome.html')

@app.route('/institutionHome')
def institutionHome():
    return render_template('institutionHome.html')

@app.route('/internship')
def internship():
    return render_template('internship.html')

@app.route('/bursary')
def bursary():
    return render_template('bursary.html')

@app.route('/shadowing')
def shadowing():
    return render_template('shadowing.html')

@app.route('/grad')
def grad():
    return render_template('grad.html')

if __name__ == '__main__':
    app.run(debug=True)
