from flask import Blueprint, render_template, request, redirect, url_for
from . import database as db
from common.count_row import count_row_per_page
from common.get_page import get_page_now

user_bp = Blueprint('user', __name__, template_folder='../templates/user' )

@user_bp.route('/')
def index():
    total = db.get_user_count()
    limit = 10
    total_page = count_row_per_page(total, limit) 
    page_now = get_page_now()   
    users = db.get_users_per_page(page_now, limit)
    return render_template('user.html', users=users,  total_page=total_page,page_now=page_now)

@user_bp.route('/search')
def search_user():
    name = request.args.get('name', default='', type=str).strip()
    if (len(name) == 1) or (len(name) == 3):
        search_result = db.search_name_from_front(name) 
    elif len(name) == 2:
        search_result = db.search_name_from_front(name) + db.search_lastname(name)
        if not search_result:  return redirect(url_for('search_user'))
    else: search_result = []    

    gender = request.args.get('gender', default='')
    if not gender:
        search_result = search_result
    elif gender == 'male':
        search_result = [r for r in search_result if r['Gender'] == 'Male']
    elif gender == 'female':
        search_result = [r for r in search_result if r['Gender'] == 'Female']

    search_result_total = len(search_result)
    limit = 10
    total_page = count_row_per_page(search_result_total, limit)
    page_now = get_page_now()
    users = search_result[(page_now-1)*limit:page_now*limit]

    return render_template('search.html', users = users,  total_page=total_page, page_now=page_now, name=name, gender=gender)
    
    
    