def count_row_per_page(total_count, rows_per_page):
    div = total_count // rows_per_page
    mod = total_count % rows_per_page
    return div, mod

