from flask import abort, render_template, redirect, request, url_for 
from flask_login import login_required

from . import home
from ..models import Student, Professional, organisation
from .forms import StudentRegistrationForm

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
    return render_template('home.html')

@home.route('/register/student', methods=['GET', 'POST'])
def student_register():
    if request.method == "POST":     

        student = Student(name = request.form.get("name"),
                    surname = request.form.get("surname"),
                    email = request.form.get("contact"),
                    sugdeg = request.form.get("subdeg"),
                    location = request.form.get("location"),
                    password = request.form.get("password"),
                    grade_year = request.form.get("password"),
                    mentor = request.form.get("password"))

        db.session.add(student)
        db.session.commit()

        print(student)

        return redirect(request.url)

     # load student registration template
    return render_template('student.html')

@home.route('/register/professional', methods=['GET', 'POST'])
def professional_register():
    return 'redirect(\'professional/dashboard\')'

@home.route('/register/institution', methods=['GET', 'POST'])
def institution_register():
    return 'redirect(\'institution/dashboard\')'

@home.route('student/dashboard')
@login_required
def student_dashboard():
    # return render_template('home/student.html')
    return 'student homepage'

@home.route('professional/dashboard')
@login_required
def professional_dashboard():
    # return render_template('home/professional.html')
    return 'professional\'s home page'

@home.route('institution/dashboard')
@login_required
def institution_dashboard():
    # return render_template('home/institution.html')
    return 'institution\'s home page'