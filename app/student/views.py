from flask import abort, render_template, redirect

from . import student

@student.route('/<username>')
def student_profile(name):
    
    #would have preferred a unique identifier such as username

    student = Student.query.filter_by(name=name).first() 
    return 'this is a student profile'

@student.route('/home')
def student_home():
    return render_template('home.html')

@student.route('/network')
def network():
    return render_template('network.html')