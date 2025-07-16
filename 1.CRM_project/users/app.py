from flask import Flask, render_template, request, redirect, url_for
import database as db
from bring_user import bring_user_in_page

app = Flask(__name__)

@app.route('/')
def index():
    total_user = db.get_user_count()
    page_now = request.args.get('page', default=1, type=int)
    users_per_page = 10
    div = total_user // users_per_page
    mod = total_user % users_per_page
    # print(div, mod)
    users = db.get_users_per_page(page_now, users_per_page)
    return render_template('user.html', users = users, div = div, mod = mod, page_now=page_now)

@app.route('/search')
def search_user():
    name = request.args.get('name', default='', type=str).strip()
    if len(name) == 1:
        search_result = len( db.search_name_from_front(name) )
    elif len(name) == 2:
        search_result = len( db.search_name_from_front(name) + db.search_lastname(name) )
        if search_result : return len(search_result)
        else : return redirect(url_for('search_user'))

    users, div, mod, page_now = bring_user_in_page(search_result)
    print(div)
    return render_template('search.html', users = users, div = div, mod = mod, page_now=page_now)

    
    # return redirect(url_for('search_user'))


if __name__ == '__main__':
    app.run(debug=True)
    # pass
    