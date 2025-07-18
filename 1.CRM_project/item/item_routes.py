from flask import Blueprint, render_template
from . import database as db

item_bp = Blueprint('item', __name__, template_folder='../templates/item')

@item_bp.route('/')
def index():
    items = db.get_items()
    return render_template('item.html', items=items)
    