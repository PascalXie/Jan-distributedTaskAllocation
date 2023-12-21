# utility : import my agent status 
import json

def GetMyAgentName(path, file_name):
    # step 0 : prepare variables for the status of agents
    my_agent_name = 'Error! Has not been given a name!'

    # step 1 : open file and get information
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_my_agent_information:
        dict_my_agent_information = json.load(json_file_my_agent_information)

        my_agent_name = dict_my_agent_information["my_agent_name"]

        # debug
        #print(type(dict_my_agent_information))
        #print(dict_my_agent_information)

    
    return my_agent_name

def GetMyAgentSamplingTimeInterval(path, file_name):
    # step 0 : prepare variables for the status of agents
    my_sampling_time_interval_unit_second = 1.

    # step 1 : open file and get information
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_my_agent_information:
        dict_my_agent_information = json.load(json_file_my_agent_information)

        my_sampling_time_interval_unit_second = dict_my_agent_information["my_sampling_time_interval_unit_second"]

        # debug
        #print(type(dict_my_agent_information))
        #print(dict_my_agent_information)

    
    return my_sampling_time_interval_unit_second

def GetMyConfidencesToAllTargets(path, file_name):
    # step 0 : prepare variables for the status of agents
    my_confidences_to_all_targets = {}

    # step 1 : open file and get confidences 
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_my_agent_information:
        dict_my_agent_information = json.load(json_file_my_agent_information)

        my_confidences_to_all_targets = dict_my_agent_information["my_confidences_to_all_targets"]

        # debug
        #print(type(dict_my_agent_information))
        #print(dict_my_agent_information)

    
    return my_confidences_to_all_targets

def GetMyAgentStatus(path, file_name):
    # step 0 : prepare variables for the status of agents
    my_agent_status = {}

    # step 1 : open file and get confidences 
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_my_agent_information:
        dict_my_agent_information = json.load(json_file_my_agent_information)

        my_agent_status = dict_my_agent_information

    return my_agent_status

if __name__ == "__main__":
    # step 1 : get information of my agents
    path = '../data/'
    file_name = 'my_agent_status.json'

    my_agent_name = GetMyAgentName(path, file_name)
    print('my_agent_name: ',my_agent_name)

    my_sampling_time_interval_unit_second = GetMyAgentSamplingTimeInterval(path, file_name)
    print('my_sampling_time_interval_unit_second: ',my_sampling_time_interval_unit_second)

    my_confidences_to_all_targets = GetMyConfidencesToAllTargets(path, file_name)
    print('my_confidences_to_all_targets: ',my_confidences_to_all_targets)

