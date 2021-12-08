import json
import pathlib
import yaml

class ValidPeople:
    data: list

    def __init__(self, path: pathlib.Path) -> None:
        self.data = json.load(open(path, encoding='cp1251'))



def insertion_sort(nums, flag:str):
    nums=nums[:10]
    # Сортировка начинается со 2-го элемента, так как по умолчанию считается, что 1-й элемент уже отсортирован
    for i in range(1, len(nums)):
        item_to_insert = nums[i][flag]
        # Сохраняется ссылка на индекс предыдущего элемента
        j = i - 1
        # Элементы сортированного сегмента перемещаются вперёд, если они больше, чем элемент для вставки
        while j >= 0 and nums[j][flag] > item_to_insert:
            nums[j + 1][flag] = nums[j][flag]
            j -= 1
        # Вставляется элемент
        nums[j + 1][flag] = item_to_insert
    return nums


def write(path,array):
    with open(path, 'w') as write_file:
        yaml.dump(array, write_file, default_flow_style=False)

def read(path):
    with open(path, 'r') as read_file:
        yaml.safe_load(read_file)

valid_data = ValidPeople(pathlib.Path("correct_data.txt"))
sort_data = insertion_sort(valid_data.data, "weight")
print(sort_data)
json.dump(
    sort_data,
    open(
        "result_sort.txt", "w"),indent=4)

write("serial.yaml", sort_data)
readfile = read(pathlib.Path('serial.yaml'))












