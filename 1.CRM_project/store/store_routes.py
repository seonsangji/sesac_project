from flask import Blueprint, render_template
from . import database as db
from common.count_row import count_row_per_page
from common.get_page import get_page_now

store_bp = Blueprint('store', __name__, template_folder='../templates/store')

@store_bp.route('/')
def index():
    total = db.get_store_count()
    stores_per_page = 10
    div, mod = count_row_per_page(total, stores_per_page) 
    page_now = get_page_now()
    stores = db.get_stores_per_page(page_now, stores_per_page)
    return render_template('store.html', stores=stores, div=div, mod=mod, page_now=page_now)