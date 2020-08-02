from flask import abort, render_template, redirect

from . import student

@student.route('/<username>')
def student_profile(username):
    student = Student.query.filter_by(username=username).first()

    return 'this is a student profile'

@student.route('/')
def student_login(uername):
    student = Student.query.filter_by(username=username).first()

    return 'this is a student profile'

@student.route('/home')
def student_home():
    return render_template('home.html')