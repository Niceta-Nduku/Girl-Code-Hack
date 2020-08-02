from flask import Blueprint

professional = Blueprint('professional', __name__)

from . import views