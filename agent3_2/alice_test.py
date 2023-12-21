# json
import json
print('hello')

current_agent_status_json = '{"name":"Agent #3", "target":"target 1"}'
print('current_agent_status_json', current_agent_status_json)


print(json.loads(current_agent_status_json))


# import a json file
path = "./data/"
file_name = "current_agent_status.json"

dict_current_agent_status = {}

with open(path+file_name, 'r', encoding='UTF-8') as json_file_current_agent_status:
    dict_current_agent_status = json.load(json_file_current_agent_status)
    print(type(dict_current_agent_status))
    print(dict_current_agent_status)

print('name: ', dict_current_agent_status["name"])
print('target: ', dict_current_agent_status["target"])

# transfer the dictionary of python into json
json_current_agent_status = json.dumps(dict_current_agent_status, sort_keys=True)
print('json_current_agent_status', type(json_current_agent_status), json_current_agent_status)
