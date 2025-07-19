from flask import Blueprint, render_template, redirect
from . import database as db

item_bp = Blueprint('item', __name__, template_folder='../templates/item')

@item_bp.route('/')
def index():
    items = db.get_items()
    return render_template('item.html', items=items)

@item_bp.route('/detail/<string:itemId>')
def get_item_detail(itemId):
    item_dict = db.get_item_info(itemId)
    rev_dict = db.get_item_rev(itemId)
    return render_template('item/detail.html', item=item_dict, rev=rev_dict)


    