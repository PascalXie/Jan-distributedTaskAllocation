# utility : export my agent's status into a file
import json

def ExportMyAgentStatusIntoAFile(dict_new_data, path, file_name):
    # step 0 : prepare variables for the status of agents
    dict_my_agent_information = {}

    # step 1 : open file and get information
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_my_agent_information:
        dict_my_agent_information = json.load(json_file_my_agent_information)

        #my_agent_name = dict_my_agent_information["my_agent_name"]

        # debug
        #print(type(dict_my_agent_information))
        #print(dict_my_agent_information)

    # step 2 : change the information of the dict_my_agent_information according to the dict_new_data
    # step 2.1 : get one key  from dict_new_data
    for element in dict_new_data:

        # step 2.2 : skip the key if it is not in the agent status
        if element not in dict_my_agent_information:
            continue

        # step 2.3 : change values of the key
        dict_my_agent_information[element] = dict_new_data[element]

    # step 3 : export the changed agent status into the file
    with open(path+file_name, 'w', encoding='UTF-8') as json_file_my_agent_information:
        json.dump(dict_my_agent_information, json_file_my_agent_information, indent=4)

    return

if __name__ == "__main__":
    print('hello')

    # step 1 : get information of my agents
    path = '../data/'
    file_name = 'my_agent_status_test.json'

    dict_new_data = {}
    dict_new_data["my_agent_location"] = {
        "x":10,
        "y":20,
        "z":30}

    ExportMyAgentStatusIntoAFile(dict_new_data, path, file_name)
