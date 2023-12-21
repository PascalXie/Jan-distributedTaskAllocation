# utility : import agent HOST and PORT
import json

def GetAllAgentInformaion(path, file_name):
    # step 0 : prepare variables for the status of agents


    # step 1 : open file and get information
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_all_agent_information:
        dict_all_agent_information = json.load(json_file_all_agent_information)

        # debug
        #print(type(dict_all_agent_information))
        #print(dict_all_agent_information)
        # !debug

        for agent_name in dict_all_agent_information:
            print(agent_name)
    
    return dict_all_agent_information

if __name__ == "__main__":
    # step 1 : get information of all agents
    path = '../data/'
    #file_name = 'all_agents_ip_port.json'
    file_name = 'all_agents_ip_port_test.json'
    dict_all_agent_information = GetAllAgentInformaion(path, file_name)

    # step 2 : get information of current agent
    my_agent_name = "Agent#3"
    my_agent_HOST = dict_all_agent_information[my_agent_name]["HOST"]
    my_agent_PORT = dict_all_agent_information[my_agent_name]["PORT"]
    print('my_agent_name: ',my_agent_name)
    print('my_agent_HOST: ',my_agent_HOST)
    print('my_agent_PORT: ',my_agent_PORT)
