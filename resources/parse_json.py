import json

def parse_json(filename) -> object:
    with open(filename) as user_file:
        file_contents = user_file.read()
    return json.loads(file_contents)