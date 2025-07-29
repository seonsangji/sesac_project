def count_row_per_page(total, limit):
    div = total // limit
    mod = total % limit
    if mod == 0:
        return div
    elif 0 < mod < limit:
        return div+1


