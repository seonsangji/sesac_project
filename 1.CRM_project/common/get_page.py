from flask import request
def get_page_now():
    page = request.args.get('page', default=1, type=int)
    if page < 1:
        return 1
    else: return page