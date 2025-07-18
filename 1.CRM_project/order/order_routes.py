from flask import Blueprint, render_template
from . import database as db
from common.get_page import get_page_now
from common.count_row import count_row_per_page

order_bp = Blueprint('order', __name__, template_folder='../templates/order')

@order_bp.route('/')
def index():
    total = db.get_order_count()
    limit = 10
    total_page = count_row_per_page(total, limit)
    page_now = get_page_now()
    items = db.get_orders_per_page(page_now,limit)
    return render_template('order.html', items=items, total_page=total_page, page_now=page_now)

    
     
