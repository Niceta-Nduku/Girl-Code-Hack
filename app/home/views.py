from flask import abort, render_template, redirect, request, url_for 
from flask_login import login_required

from . import home
from ..models import Student, Professional, organisation, Interests, locations

@home.route ('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('signin.html')

@home.route('/register')
def register():
    return render_template('signup.html')

@home.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == "POST":
        
    return redirect(url_for('student.student_login'))

@home.route('/register/student', methods=['GET', 'POST'])
def student_register():
    if request.method == "POST":    

        input_interest = Interests.query.filter_by(description=request.form.get("interests")).one()

        student = Student(name = request.form.get("name"),
                    surname = request.form.get("surname"),
                    interests = input_interest,
                    email = request.form.get("contact"),                   
                    sugdeg = request.form.get("subdeg"),
                    location = request.form.get("location"),
                    password = request.form.get("password"),
                    grade_year = request.form.get("password"),
                    mentor = request.form.get("password"))

        db.session.add(student)
        db.session.commit()

        print("Added student")

        return redirect(request.url)

     # load student registration template
    return render_template('student.html')

@home.route('/register/professional', methods=['GET', 'POST'])
def professional_register():
    return render_template('mentor.html')

@home.route('/register/institution', methods=['GET', 'POST'])
def institution_register():
    return render_template('institution.html')


@home.route('student/home')
@login_required
def student_home():
    return render_template('home.html')


@home.route('professional/home')
@login_required
def professional_home():
    return render_template('MentorHome.html')

@home.route('institution/home')
@login_required
def institution_home():
    return render_template('institutionHome.html')