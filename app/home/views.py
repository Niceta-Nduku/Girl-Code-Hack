from flask import abort, render_template, redirect
from flask_login import login_required

from . import home
from ..models import Student, Professional, organisation
from .forms import StudentRegistrationForm

@home.route ('/')
def homepage():
    """
    Render the homepage template on the / route
    """
    return render_template('home.html')

@home.route('/register')
def register():
    return render_template('signup.html')

@home.route('/register/student', methods=['GET', 'POST'])
def student_register():
    form = StudentRegistrationForm()
    if form.validate_on_submit():
        student = Student()

        db.session.add(student)
        db.session.commit()

        #login
        return redirect('student/dashboard')

     # load student registration template
    return render_template('student.html', form=form, title='Student Registration')

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