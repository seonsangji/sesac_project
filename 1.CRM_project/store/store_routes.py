from flask import Blueprint, render_template, request, redirect, url_for
from . import database as db
from common.count_row import count_row_per_page
from common.get_page import get_page_now
from common.set_pagination import set_pagination

store_bp = Blueprint('store', __name__, template_folder='../templates/store')

@store_bp.route('/')
def index():
    total = db.get_store_count()
    limit = 10
    total_page = count_row_per_page(total, limit)

    query_args = request.args.to_dict()
    raw_page = query_args.get('page')
    page_now = get_page_now()

    if (raw_page is None) or (str(page_now) != raw_page):
        query_args['page'] = 1
        return redirect(url_for(request.endpoint, **query_args))

    stores = db.get_stores_per_page(page_now, limit)
    start, stop = set_pagination(page_now, total_page)
    return render_template(
        'store.html', 
        stores=stores, 
        total_page=total_page, 
        page_now=page_now,
        start=start,
        stop=stop,
        query_args=query_args,
        view_name='store.index'
        )

@store_bp.route('/detail/<string:storeId>')
def get_store_detail(storeId):
    store_dict = db.get_store_info(storeId)

    rev_month = request.args.get('rev_month', default='')

    if rev_month == '':
        rev_dict = db.get_store_rev(storeId)
        user_dict = db.get_user_list_by_storeId(storeId)
        return render_template('store/detail.html', store=store_dict, rev= rev_dict, users = user_dict)
    else :
        rev_month_dict = db.get_store_rev_for_month(rev_month, storeId)
        user_month_dict = db.get_user_list_by_storeId_for_month(rev_month, storeId) 
        return render_template('store/detail.html', store=store_dict, rev= rev_month_dict, users = user_month_dict)