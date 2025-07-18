from flask import Blueprint, render_template
from . import database as db
from common.count_row import count_row_per_page
from common.get_page import get_page_now

orderitem_bp = Blueprint('orderitem', __name__, template_folder='../templates/orderitem')

@orderitem_bp.route('/')
def index():
    total = db.get_orderitem_count()
    limit = 10
    total_page = count_row_per_page(total, limit)
    page_now = get_page_now()
    orderitems = db.get_orderitems_per_page(page_now, limit)
    return render_template('orderitem.html', orderitems=orderitems, total_page=total_page, page_now=page_now)

@orderitem_bp.route('/detail/<string:orderId>')
def get_orderitem_detail(orderId):
    orderitem_dict = db.get_orderitem_info_by_orderId(orderId)
    print(orderitem_dict)
    return render_template('orderitem/detail.html',orderitems=orderitem_dict)
