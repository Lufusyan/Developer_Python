# TODO импортировать необходимые молули
import json
import csv


INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    my_data = []
    with open(INPUT_FILENAME, encoding='utf-8') as f:
        file_ = csv.DictReader(f)
        for rows in file_:
            my_data.append(rows)
    with open(OUTPUT_FILENAME, 'w', encoding="utf-8") as file:
        json.dump(my_data, file, indent=4, ensure_ascii=False)

    # TODO считать содержимое csv файла

    ...  # TODO Сериализовать в файл с отступами равными 4


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
