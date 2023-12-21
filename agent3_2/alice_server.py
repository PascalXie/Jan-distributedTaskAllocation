# server
import socketserver
import json

# preparation for importing utilities
import sys
sys.path.append("./utilities")

# importing utilities
from import_agent_host_and_port import *
#from import_my_agent_name import *
from import_my_agent_status import *
from import_my_program_verbose_level import *

class MyTCPHandler(socketserver.BaseRequestHandler):

    def handle(self):
        # 接收客户端请求的数据
        self.data = self.request.recv(1024).strip()
        print("{} 发送了：{}".format(self.client_address[0], self.data))

        # 向客户端发送响应数据
        json_current_agent_status = self.GetMyCurrentStatus()

        self.request.sendall(json_current_agent_status.encode('utf-8'))


    def GetMyCurrentStatus(self):

        # step 1 : import the json file
        path = "./data/"
        file_name = "my_agent_status.json"
        
        dict_current_agent_status = {}
        
        with open(path+file_name, 'r', encoding='UTF-8') as json_file_current_agent_status:
            dict_current_agent_status = json.load(json_file_current_agent_status)

            # debug
            #print(type(dict_current_agent_status))
            #print(dict_current_agent_status)
            # !debug
        
        # transfer the dictionary of python into json
        json_current_agent_status = json.dumps(dict_current_agent_status, sort_keys=True)
        
        return json_current_agent_status 

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

    print('does_debug: ',does_debug)
    print('my_program_verbose_level: ',my_program_verbose_level)

    #
    # step 1 : get information of all agents
    #
    path = './data/'

    file_name = ''
    if does_debug == 0:
        file_name = 'all_agents_ip_port.json'
    else:
        file_name = 'all_agents_ip_port_test.json'

    print("----")
    print("------------")
    print("step 1 : get information of all agents")
    print("------------")
    print("----")

    print("file_name: ", file_name)

    dict_all_agent_information = GetAllAgentInformaion(path, file_name)

    #
    # step 2 : get information of my agent
    #
    print("----")
    print("------------")
    print("step 2 : get information of my agent")
    print("------------")
    print("----")

    # step 2.1 : get my agent name
    path_my_agent_name_file = './data/'
    file_name_my_agent_name_file = 'my_agent_status.json'

    my_agent_name = GetMyAgentName(path_my_agent_name_file, file_name_my_agent_name_file)

    # step 2.2 : get my agent information, including HOST and PORT
    my_agent_HOST = dict_all_agent_information[my_agent_name]["HOST"]
    my_agent_PORT = dict_all_agent_information[my_agent_name]["PORT"]

    print("----")
    print("------------")
    print("step 2.2 : get my agent information, including HOST and PORT")
    print("------------")
    print("----")

    print('my_agent_name: ',my_agent_name)
    print('my_agent_HOST: ',my_agent_HOST)
    print('my_agent_PORT: ',my_agent_PORT)


    #
    # step 3 : start a server 
    #
    print("----")
    print("------------")
    print("step 3 : start a server")
    print("------------")
    print("----")
    server = socketserver.TCPServer((my_agent_HOST, my_agent_PORT), MyTCPHandler)

    # 启动服务器
    print("Server is going to be started...")
    server.serve_forever()
