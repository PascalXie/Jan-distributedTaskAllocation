# utility : import verbose level of my program 

import json

def GetMyProgramVerboseLevel(path, file_name):
    # step 1 : open file and get information
    with open(path+file_name, 'r', encoding='UTF-8') as json_file_my_program_verbose_level:
        dict_my_program_verbose_level = json.load(json_file_my_program_verbose_level)

    return dict_my_program_verbose_level

if __name__ == "__main__":
    # step 1 : get information of my agents
    path = '../data/'
    file_name = 'my_program_verbose_level.json'
    dict_my_program_verbose_level = GetMyProgramVerboseLevel(path, file_name)

    is_debug = dict_my_program_verbose_level["is_debug"]
    my_program_verbose_level = dict_my_program_verbose_level["verboose_level"]

    print('is_debug: ',is_debug)
    print('my_program_verbose_level: ',my_program_verbose_level)
