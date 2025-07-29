def set_pagination(page_now, total_page):
    if page_now <= 2:
        return 1, 5
    elif total_page-1 <= page_now <= total_page:
        return total_page-4, total_page +1
    else:
        return page_now-2, page_now+2