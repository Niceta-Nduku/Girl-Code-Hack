from flask import abort, render_template, redirect

from . import institution


@institution.route('/home')
def institution_home():
    return render_template('institutionHome.html')