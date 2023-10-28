# TODO Напишите функцию для поиска индекса товара
def find_index_product(list_product, find_product):
    index = None
    for i in range(len(list_product)):
        if list_product[i] == find_product:
            index = i
            break
    return index

items_list = ['яблоко', 'банан', 'апельсин', 'груша', 'киви', 'банан']

for find_item in ['банан', 'груша', 'персик']:
    index_item = find_index_product(items_list, find_item)  # TODO Вызовите функцию, что получить индекс товара
    if index_item is not None:
        print(f"Первое вхождение товара '{find_item}' имеет индекс {index_item}.")
    else:
        print(f"Товар '{find_item}' не найден в списке.")
