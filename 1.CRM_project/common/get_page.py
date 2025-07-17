from flask import request

def get_page_now():
    return request.args.get('page', default=1, type=int)
    