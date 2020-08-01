from flask import abort, render_template, redirect

from . import opportunity

@opportunity.route ('opportunities/internships')
def internships():
    return render_template('internship.html')

@opportunity.route ('opportunities/bursary')
def bursary():
    return render_template('bursary.html')

@opportunity.route ('opportunities/shadowing')
def shadowing():
    return render_template('shadowing.html')

@opportunity.route ('opportunities/grad')
def grad():
    return render_template('grad.html')