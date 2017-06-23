import json
from pprint import pprint

with open('resources/sample_json_file.json') as data_file:
    data = json.load(data_file)
pprint(data)


# import json
#
# with open('sample_json_file.json', 'r') as inline:
#     jsonData = inline.read()
#
# content = jsonData
# dumped = json.dumps(content)
# loaded = json.loads(dumped)
#
# for data in loaded:
#     print(data)
