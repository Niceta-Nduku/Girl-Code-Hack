from flask import abort, render_template, redirect

from . import professional

@professional.route('/<username>')
def professional_profile(name):
    
    #would have preferred a unique identifier such as username

    professional = professional.query.filter_by(name=name).first() 
    return 'this is a professional profile'

@professional.route('/home')
def professional_home():
    return render_template('MentorHome.html')