from flask import Blueprint, render_template
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
    month = [ d['Month'] for d in rev_dict ]
    rev_data = [ d['TotalRevenue'] for d in rev_dict]
    count = [ d['ItemCount'] for d in rev_dict]
    return render_template('item/detail.html', item=item_dict, rev=rev_dict, month=month, rev_data=rev_data, count=count)
    