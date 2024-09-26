import json

data = '{"key1": 1, "key2": 2, "key3": [1, 2, 3]}'
parsed_data = json.loads(data)
print(type(data))
print(type(parsed_data))