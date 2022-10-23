from flask import Blueprint
from app.controllers import test

bp = Blueprint('test',__name__)

bp.route('/', methods=['GET'])(test.test)
