from flask import Blueprint, render_template, request, redirect, url_for
from . import database as db
from common.get_page import get_page_now
from common.count_row import count_row_per_page
from common.set_pagination import set_pagination

order_bp = Blueprint('order', __name__, template_folder='../templates/order')

@order_bp.route('/')
def index():
    total = db.get_order_count()
    limit = 10
    total_page = count_row_per_page(total, limit)

    query_args = request.args.to_dict()
    raw_page = query_args.get('page')
    page_now = get_page_now()

    if (raw_page is None) or ( str(page_now) != raw_page):
        query_args['page'] = 1
        return redirect(url_for(request.endpoint, **query_args))
    
    orders = db.get_orders_per_page(page_now,limit)
    start, stop = set_pagination(page_now, total_page)
    return render_template(
        'order.html',
        orders=orders, 
        total_page=total_page, 
        page_now=page_now,
        start=start,
        stop=stop,
        query_args=query_args,
        view_name='order.index'
        )

@order_bp.route('/detail/<string:orderId>')
def get_order_detail(orderId):
    order_dict = db.get_order_info(orderId)
    return render_template('order/detail.html', order=order_dict)

    
     
