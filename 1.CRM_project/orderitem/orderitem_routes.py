from flask import Blueprint, render_template, request, redirect, url_for
from . import database as db
from common.count_row import count_row_per_page
from common.get_page import get_page_now
from common.set_pagination import set_pagination

orderitem_bp = Blueprint('orderitem', __name__, template_folder='../templates/orderitem')

@orderitem_bp.route('/')
def index():
    total = db.get_orderitem_count()
    limit = 10
    total_page = count_row_per_page(total, limit)

    query_args = request.args.to_dict()
    raw_page = query_args.get('page')
    page_now = get_page_now()

    if (raw_page is None) or (str(page_now) != raw_page):
        query_args['page'] = 1
        return redirect(url_for(request.endpoint, **query_args))
    
    orderitems = db.get_orderitems_per_page(page_now, limit)
    start, stop = set_pagination(page_now, total_page)
    return render_template(
        'orderitem.html', 
        orderitems=orderitems, 
        total_page=total_page,
        page_now=page_now,
        start=start,
        stop=stop,
        query_args=query_args,
        view_name='orderitem.index'
        )

@orderitem_bp.route('/detail/<string:orderId>')
def get_orderitem_detail(orderId):
    orderitem_dict = db.get_orderitem_info_by_orderId(orderId)
    print(orderitem_dict)
    return render_template('orderitem/detail.html',orderitems=orderitem_dict)
