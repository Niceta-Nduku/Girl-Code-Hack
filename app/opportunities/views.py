from flask import abort, render_template, redirect

from . import opportunity

@opportunity.route ('/internships')
def internships():
    return render_template('internship.html')

@opportunity.route ('/bursary')
def bursary():
    return render_template('bursary.html')

@opportunity.route ('/shadowing')
def shadowing():
    return render_template('shadowing.html')

@opportunity.route ('/grad')
def grad():
    return render_template('grad.html')