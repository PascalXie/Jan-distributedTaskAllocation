# utility : import agent HOST and PORT
import json

def GetMyAgentName(path, file_name):
    # step 0 : prepare variables for the status of agents


    # step 1 : open file and get information
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_my_agent_information:
        dict_my_agent_information = json.load(json_file_my_agent_information)

        # debug
        #print(type(dict_my_agent_information))
        #print(dict_my_agent_information)
    
    return dict_my_agent_information

if __name__ == "__main__":
    # step 1 : get information of my agents
    path = '../data/'
    file_name = 'my_agent_status.json'
    dict_my_agent_information = GetMyAgentName(path, file_name)

    my_agent_name = dict_my_agent_information["my_agent_name"]

    print('my_agent_name: ',my_agent_name)
