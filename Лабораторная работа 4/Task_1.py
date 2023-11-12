# TODO решите задачу
import json

def task() -> float:
    with open("input.json") as f:
        json_data = json.load(f)
    summa = sum([item["score"]*item["weight"] for item in json_data])
    return round(summa, 3)


print(task())
