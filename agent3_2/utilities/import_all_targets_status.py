# utility : import all targets' status 
import json

def GetAllTargetsStatus(path, file_name):
    # step 0 : prepare variables for the status of agents
    all_targets_status = {}

    # step 1 : open file and get confidences 
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_all_targets_status:
        dict_all_targets_status = json.load(json_file_all_targets_status)

    return dict_all_targets_status

if __name__ == "__main__":
    # step 1 : get information of my agents
    path = '../data/'
    file_name = 'all_observed_targets_information.json'

    dict_all_targets_status = GetAllTargetsStatus(path, file_name)
    print('dict_all_targets_status: ', dict_all_targets_status)
