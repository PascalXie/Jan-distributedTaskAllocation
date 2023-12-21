# client
import socket
import json
import time
# preparation for importing utilities
import sys
sys.path.append("./utilities")

# importing utilities
from import_agent_host_and_port import *
from import_my_agent_status import *
from import_my_program_verbose_level import *

# import utilities of calculate_confidences 
from calculate_confidences import *


def AskAgentForStatus(HOST, PORT, my_agent_name):

    # step 0 : prepare the information for connection
    string_data_to_be_sent = "HEllo, this is " +  my_agent_name+ ". I'm asking for your current status..."

    # step 1 : connect the server
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((HOST, PORT))
        s.sendall(string_data_to_be_sent.encode('utf-8'))
        data = s.recv(1024).decode('utf-8')


    # decoding the json to dict
    dict_current_agent_status = json.loads(data)

    #print("The current status has been recieved. Thank you!")
    #print("The current status is shown below.")
    #print(dict_current_agent_status)

    return dict_current_agent_status


if __name__ == "__main__":
    #
    # step 0 : get debug information 
    #
    path = './data/'
    file_name = 'my_program_verbose_level.json'
    dict_my_program_verbose_level = GetMyProgramVerboseLevel(path, file_name)

    does_debug = dict_my_program_verbose_level["does_debug"]
    my_program_verbose_level = dict_my_program_verbose_level["verbose_level"]

    print("----")
    print("------------")
    print("step 0 : get debug information")
    print("------------")
    print("----")

    print("does_debug: ", does_debug)
    print("my_program_verbose_level: ", my_program_verbose_level, type(my_program_verbose_level))

    #
    # step 1 : get information of all agents
    #
    path = './data/'

    file_name = ''
    if does_debug == 0:
        file_name = 'all_agents_ip_port.json'
    else:
        file_name = 'all_agents_ip_port_test.json'


    print("\n----")
    print("------------")
    print("step 1 : get information of all agents")
    print("------------")
    print("----")

    print("file_name: ", file_name)

    dict_all_agent_information = GetAllAgentInformaion(path, file_name)

    #
    # step 2 : get information of my agent
    #
    print("\n----")
    print("------------")
    print("step 2 : get information of my agent")
    print("------------")
    print("----")

    # step 2.1 : get my agent name
    path_my_agent_status_file = './data/'
    file_name_my_agent_status_file = 'my_agent_status.json'

    my_agent_name = GetMyAgentName(path_my_agent_status_file, file_name_my_agent_status_file)

    print("----")
    print("------------")
    print("step 2.1 : get my agent name")
    print("------------")
    print("----")

    print('my_agent_name: ',my_agent_name)

    # step 2.2 : get my agent information, including HOST and PORT
    my_agent_HOST = dict_all_agent_information[my_agent_name]["HOST"]
    my_agent_PORT = dict_all_agent_information[my_agent_name]["PORT"]

    print("----")
    print("------------")
    print("step 2.2 : get my agent information, including HOST and PORT")
    print("------------")
    print("----")

    print('my_agent_HOST: ',my_agent_HOST)
    print('my_agent_PORT: ',my_agent_PORT)

    # step 2.3 : get my agent information, including my_sampling_time_interval_unit_second
    my_sampling_time_interval_unit_second = GetMyAgentSamplingTimeInterval(path_my_agent_status_file, file_name_my_agent_status_file)
    print("----")
    print("------------")
    print("step 2.3 : get my agent information, including my_sampling_time_interval_unit_second")
    print("------------")
    print("----")

    print('my_sampling_time_interval_unit_second: ',my_sampling_time_interval_unit_second)


    #
    # step 3 : asking ohter agents for thier current information
    #
    print("\n----")
    print("------------")
    print("step 3 : asking ohter agents for thier current information")
    print("------------")
    print("----")
    for i in range(30):

        # step 3.1 : get my agent's previous confidence, which was written in the file, file_name_my_agent_status_file
        my_confidences_to_all_targets = GetMyConfidencesToAllTargets(path_my_agent_status_file, file_name_my_agent_status_file)
        print('step 3.1 : get my agents previous confidence, which was written in the file, file_name_my_agent_status_file')
        print('my_confidences_to_all_targets: ',my_confidences_to_all_targets)

        # step 3.1.2 : prepare a variable that recoreds the confidences of the neighbour agents 
        neighbour_agents_confidences_to_all_targets = {} # {'target_name': [agent#i_confidence, agent#j_confidence, ...]}
        for my_target_name in my_confidences_to_all_targets:
            neighbour_agents_confidences_to_all_targets[my_target_name] = []

        print('step 3.1.2 : prepare a variable that recoreds the confidences of the neighbour agents')
        print('neighbour_agents_confidences_to_all_targets', neighbour_agents_confidences_to_all_targets)

        # step 3.2 : ask agents in the neighbour set for their information 
        for current_agent_name in dict_all_agent_information:
    
            # step (1) : skip the current agent
            if  current_agent_name == my_agent_name:
                continue

            # step (2) : get information
            current_agent_HOST = dict_all_agent_information[current_agent_name]["HOST"]
            current_agent_PORT = dict_all_agent_information[current_agent_name]["PORT"]
    
            # debug
            #print("current_agent_name, HOST and PORT: ", current_agent_name, current_agent_HOST, ', ',  current_agent_PORT)
            # !debug

            dict_current_agent_status = AskAgentForStatus(current_agent_HOST, current_agent_PORT, my_agent_name)

            # debug
            #print("The current status of Agent ",my_agent_name ," has recieved and is shown below.")

            ##print(dict_current_agent_status)

            #for element in dict_current_agent_status:
            #    print(element,": ", dict_current_agent_status[element])

            # !debug

            # step (3) : get confidences and recored them into the variable "neighbour_agents_confidences_to_all_targets"
            # get confidences
            current_agent_confidences = dict_current_agent_status['my_confidences_to_all_targets']

            # recored them into the variable "neighbour_agents_confidences_to_all_targets"
            for my_target_name in my_confidences_to_all_targets:

                # make sure the target_name exist in current_agent_confidences. If the target_name does not exist, continue
                if my_target_name not in current_agent_confidences:
                    continue

                # get the confidence corresponding to the target_name 
                a_current_agent_confidence = current_agent_confidences[my_target_name]

                # record the confidence in neighbour_agents_confidences_to_all_targets
                neighbour_agents_confidences_to_all_targets[my_target_name].append(a_current_agent_confidence)


            # debug
            #current_agent_confidences = dict_current_agent_status['my_confidences_to_all_targets']
            #for element in current_agent_confidences:
            #    print(current_agent_name,', ', element,": ", current_agent_confidences[element])

            # !debug

        # debug
        print('neighbour_agents_confidences_to_all_targets (after): ', neighbour_agents_confidences_to_all_targets)
        # !debug


        # step 3.3 : do the calculation for the next confidence value of my agent
        # step 3.3.1 : set the path and file name of all_observed_targets_information.json
        path_all_observed_targets_information_file = "./data/"
        file_name_all_observed_targets_information_file = "all_observed_targets_information.json"
        my_agent = CalculateConfidences(path_my_agent_status_file, file_name_my_agent_status_file, my_confidences_to_all_targets, neighbour_agents_confidences_to_all_targets, path_all_observed_targets_information_file, file_name_all_observed_targets_information_file)
        my_agent.DoCalculation()

        # wait until the time interval ends
        time.sleep(my_sampling_time_interval_unit_second)
