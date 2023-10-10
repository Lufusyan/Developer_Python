# TODO Найдите количество книг, которое можно разместить на дискете
inf_volume = 1.44 * 1024 * 1024
count_pages_in_book = 100
number_lines_in_page = 50
count_symbols_in_line = 25
weight_one_symbols = 4
volume_one_book = count_pages_in_book*number_lines_in_page*count_symbols_in_line*weight_one_symbols
count_book = round(inf_volume // volume_one_book)
print("Количество книг, помещающихся на дискету:", count_book)
