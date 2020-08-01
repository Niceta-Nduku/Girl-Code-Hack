from flask import Blueprint

institution = Blueprint('institution', __name__)

from . import views