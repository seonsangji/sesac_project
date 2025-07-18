def count_row_per_page(total, limit):
    div = total // limit
    mod = total % limit
    total_page = div
    if mod == 0:
        total_page = div
    elif 0<mod<div:
        total_page = div+1
    return total_page


