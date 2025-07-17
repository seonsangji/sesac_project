from flask import Flask, render_template, request, redirect, url_for
import database as db
from get_and_count_page import count_user_per_page

app = Flask(__name__)

@app.route('/')
def index():
    total_user = db.get_user_count()
    users_per_page = 10
    div, mod, page_now = count_user_per_page(total_user, users_per_page)    
    users = db.get_users_per_page(page_now, users_per_page)
    return render_template('user.html', users=users, div=div, mod=mod, page_now=page_now)

@app.route('/search')
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

    search_result_count = len(search_result)
    users_per_page = 10
    div, mod, page_now = count_user_per_page(search_result_count, users_per_page)
    users = search_result[(page_now-1)*users_per_page:page_now*users_per_page]

    return render_template('search.html', users = users, div = div, mod = mod, page_now=page_now, name=name)
    


if __name__ == '__main__':
    app.run(debug=True)
    
    