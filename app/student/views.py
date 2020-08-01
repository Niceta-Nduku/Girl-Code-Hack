from flask import abort, render_template, redirect

from . import student


@student.route('/<username>')
def student_profile(username):
    student = Student.query.filter_by(username=username).first()

    return 'this is a student profile'


