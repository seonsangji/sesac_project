from flask import Blueprint, render_template, request
from . import database as db
from common.count_row import count_row_per_page
from common.get_page import get_page_now

store_bp = Blueprint('store', __name__, template_folder='../templates/store')

@store_bp.route('/')
def index():
    total = db.get_store_count()
    limit = 10
    total_page = count_row_per_page(total, limit) 
    page_now = get_page_now()
    stores = db.get_stores_per_page(page_now, limit)
    return render_template('store.html', stores=stores, total_page=total_page, page_now=page_now)

@store_bp.route('/detail/<string:storeId>')
def get_store_detail(storeId):
    store_dict = db.get_store_info(storeId)
    rev_dict = db.get_store_rev(storeId)
    user_dict = db.get_user_list_by_storeId(storeId)
    return render_template('store/detail.html', store=store_dict, rev= rev_dict, users = user_dict)

def get_store_rev_month(storeId):
    month = request.args.get('rev_month', default='')
