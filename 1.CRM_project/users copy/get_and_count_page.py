from flask import request
import database as db

def count_user_per_page(user_count, users_per_page):
    total_user = user_count
    page_now = request.args.get('page', default=1, type=int)
    div = total_user // users_per_page
    mod = total_user % users_per_page
    # print(div, mod)
    return div, mod, page_now