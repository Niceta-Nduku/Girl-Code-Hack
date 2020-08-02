from flask import abort, render_template, redirect, request, url_for 
from flask_login import login_required, login_user, logout_user

from . import home
from .. import db
from ..models import Student, Professional, organisation, Interests, locations

@home.route ('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('signin.html')

@home.route('/login',methods=['GET', 'POST'])
def login():
    if request.method == "POST": 

        student = Student.query.filter_by(email= request.form.get("contact")).first()

        if student is not None and student.verify_password(request.form.get("password")):
            login_user(student)
            return redirect(url_for('student.home'))
        else:
            flash('Invalid email or password.')

    return render_template('home.html')

@home.route('/register')
def register():
    return render_template('signup.html')

@home.route('/register/student', methods=['GET', 'POST'])
def student_register():
    if request.method == "POST":    
        
        # input_interest = Interests.query.filter_by(description=request.form.get("interests")).one()
        interest_in_mentor = request.form.get("Mentor")
        student = Student(name = request.form.get("name"),
                    username = request.form.get("surname"),
                    # interests = input_interest,
                    email = request.form.get("contact"),   
                    password = request.form.get("password"),
                    level = request.form.get("password"),
                    mentorship = True if interest_in_mentor == 'Yes' else False)

        db.session.add(student)
        db.session.commit()

        print("Added student")

        return redirect(url_for('student.student_home'))

     # load student registration template
    return render_template('student.html')

@home.route('/register/professional', methods=['GET', 'POST'])
def professional_register():
    #todo: add progessional object to db 
    return render_template('mentor.html')

@home.route('/register/institution', methods=['GET', 'POST'])
def institution_register():
    #todo: add institution object to db
    return render_template('institution.html')

@home.route('/logout')
@login_required
def logout():
    #add log out details
    logout_user()
    return redirect(url_for('home.login'))