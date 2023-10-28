# TODO Напишите функцию find_common_participants
def find_common_participants(first_group, second_group, delimiter=','):
    for i in range(len(first_group)):
        if not first_group[i].isalpha():
            delimiter = first_group[i]
    general_participants = list(set(first_group.split(delimiter)).intersection(second_group.split(delimiter)))
    general_participants.sort()
    return general_participants


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"
find_common_participants(participants_first_group, participants_second_group)
# TODO Провеьте работу функции с разделителем отличным от запятой
