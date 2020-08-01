from flask import Blueprint

opportunity = Blueprint('opportunity', __name__)

from . import views