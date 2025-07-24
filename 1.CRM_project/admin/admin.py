from flask import Blueprint, render_template

add_bp = Blueprint('add', __name__,  template_folder='../templates/admin')

@add_bp.route('/')
def add():
    pass