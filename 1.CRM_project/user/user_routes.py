from flask import Blueprint, render_template, request, redirect, url_for
from . import database as db
from common.count_row import count_row_per_page
from common.get_page import get_page_now
from common.set_pagination import set_pagination

user_bp = Blueprint('user', __name__, template_folder='../templates/user' )

@user_bp.route('/')
def index():
    total = db.get_user_count()
    limit = 10
    total_page = count_row_per_page(total, limit) 
    query_args = request.args.to_dict()
    raw_page = query_args.get('page')
    page_now = get_page_now()


    if (raw_page is None) or ( str(page_now) != raw_page):
        query_args['page'] = 1
        return redirect(url_for(request.endpoint, **query_args))
    print(f"{query_args}에서 page값 삭제 전")
    query_args.pop('page', None)
    print(f"{query_args}에서 page값 삭제 후")

    users = db.get_users_per_page(page_now, limit)
    start, stop = set_pagination(page_now, total_page)
    return render_template(
        'user.html', 
        users=users,  
        total_page=total_page,
        page_now=page_now,
        start=start, 
        stop=stop,
        query_args = query_args,
        view_name='user.index'
        )

@user_bp.route('/search')
def search_user():
    name = request.args.get('name', default='', type=str).strip()
    gender = request.args.get('gender', default='')

    if (len(name) == 1) or (len(name) == 3):
        search_result = db.search_name_from_front(name) 
    elif len(name) == 2:
        search_result = db.search_name_from_front(name) + db.search_lastname(name)
        if not search_result:  return redirect(url_for('user.search_user'))
    elif name == '' and gender != '':
        if gender == 'male':
            search_result = [r for r in db.get_users() if r['Gender'] == 'Male']
        elif gender == 'female':
            search_result = [r for r in db.get_users() if r['Gender'] == 'Female']
    else: search_result = []    

    
    if not gender:
        search_result = search_result
    elif gender == 'male':
        search_result = [r for r in search_result if r['Gender'] == 'Male']
    elif gender == 'female':
        search_result = [r for r in search_result if r['Gender'] == 'Female']

    search_result_total = len(search_result)
    limit = 10
    total_page = count_row_per_page(search_result_total, limit)

    query_args = request.args.to_dict()
    raw_page = query_args.get('page')
    page_now = get_page_now()

    if (raw_page is None) or ( str(page_now) != raw_page):
        query_args['page'] = 1
        return redirect(url_for(request.endpoint, **query_args))
    print(f"{query_args}에서 page값 삭제 전")
    query_args.pop('page', None)
    print(f"{query_args}에서 page값 삭제 후")

    users = search_result[(page_now-1)*limit:page_now*limit]
    start, stop = set_pagination(page_now, total_page)
    return render_template(
        'user/search.html', 
        users = users,  total_page=total_page, page_now=page_now, 
        name=name, 
        gender=gender,
        start=start,
        stop=stop,
        query_args=query_args,
        view_name='user.search_user'
            )
                           

@user_bp.route('/detail/<string:userId>')
def get_user_detail(userId):
    user_dict = db.get_user_info(userId)
    order_dict = db.get_order_info_by_userId(userId)
    visit_dict, ordercount_dict = db.get_user_behavior(userId)
    return render_template('user/detail.html', user=user_dict, orders=order_dict, visits = visit_dict, ordercount = ordercount_dict)



    
    