import json

data = '{"key1": 1, "key2": 2, "key3": [1, 2, 3]}'
print(type(data))
parsed_data = json.loads(data)  # преобразование строки в словарь
print(type(parsed_data))
print(parsed_data['key2'] + 1)
parsed_data['key1'] = 4
print(parsed_data)

data_dict = {
    'key': 1,
    2: 'one',
    'list': [4, 5, 6]
}
print(type(data_dict))
parsr_to_string = json.dumps(data_dict) # преобразование словаря в строку
print(type(parsr_to_string))