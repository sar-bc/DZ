import json
from random import choice


def gen_person():
    _id = ''
    name = ''
    tel = ''

    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
    nums = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

    while len(_id) != 10:
        _id += choice(nums)

    while len(name) != 7:
        name += choice(letters)

    while len(tel) != 10:
        tel += choice(nums)

    person = {
        _id: {
            'name': name,
            'tel': tel
        }
    }

    return person


def write_json(person_dict):
    try:
        data = json.load(open('persons.json'))
    except FileNotFoundError:
        data = {}

    data = data | person_dict
    with open("persons.json", "w") as f:
        json.dump(data, f, indent=2)


for i in range(5):
    write_json(gen_person())
