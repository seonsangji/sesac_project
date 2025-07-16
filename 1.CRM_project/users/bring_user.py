from flask import request
import database as db

def bring_user_in_page(user_count):
    total_user = user_count
    page_now = request.args.get('page', default=1, type=int)
    users_per_page = 10
    div = total_user // users_per_page
    mod = total_user % users_per_page
    # print(div, mod)
    users = db.get_users_per_page(page_now, users_per_page)
    return users, div, mod, page_now