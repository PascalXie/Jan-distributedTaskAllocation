# class : calculate confidences
import socket
import json
import time
# preparation for importing utilities
import sys
sys.path.append("../utilities")

# importing utilities
from import_agent_host_and_port import *
from import_my_agent_status import *
from import_my_program_verbose_level import *
from import_all_targets_status import *

class CalculateConfidences:
    def __init__(
        self, 
        path_my_agent_status_file, 
        file_name_my_agent_status_file, 
        my_confidences_to_all_targets, 
        neighbour_agents_confidences_to_all_targets, 
        path_all_observed_targets_information_file, 
        file_name_all_observed_targets_information_file):

        self.path_my_agent_status_file      = path_my_agent_status_file
        self.file_name_my_agent_status_file = file_name_my_agent_status_file

        self.neighbour_agents_confidences_to_all_targets = neighbour_agents_confidences_to_all_targets

        self.path_all_observed_targets_information_file = path_all_observed_targets_information_file
        self.file_name_all_observed_targets_information_file = file_name_all_observed_targets_information_file


        # get my agent's previous confidence, which was written in the file, file_name_my_agent_status_file
        self.my_confidences_to_all_targets = GetMyConfidencesToAllTargets(path_my_agent_status_file, file_name_my_agent_status_file)

        # set parameters
        self.epsilon = 1.


        # debug
        print("class CalculateConfidences: ")
        print('path_my_agent_status_file, file_name_my_agent_status_file',self.path_my_agent_status_file,file_name_my_agent_status_file)
        print('my_confidences_to_all_targets', self.my_confidences_to_all_targets)
        print('neighbour_agents_confidences_to_all_targets', self.neighbour_agents_confidences_to_all_targets)
        print('path_all_observed_targets_information_file, file_name_all_observed_targets_information_file', self.path_all_observed_targets_information_file , self.file_name_all_observed_targets_information_file)
        # !debug

        return

    def DoCalculation(self):
        # step 1 : get target names
        for target_name in self.my_confidences_to_all_targets:
            my_confidence = self.DoCalculationAccordingToTarget(target_name)
            print('target_name: ', target_name, ', my_confidence = ', my_confidence)

        return

    def DoCalculationAccordingToTarget(self, target_name):
        # step 0 : show target_name
        print('DoCalculationAccordingToTarget,  step 0 : show target_name, ', target_name)
    
        # step 1 : initiate parameter u
        u = 0

        # step 2 : get my previous confidence
        my_confidence = self.my_confidences_to_all_targets[target_name]
        print('my_previous_confidence: ', my_confidence)

        # step 3 : get  confidence of the neighbour agents
        confidences_neighbour_agents = self.neighbour_agents_confidences_to_all_targets[target_name]
        print('confidences_neighbour_agents: ', confidences_neighbour_agents)

        # step 4 : do calculate
        for current_neighbour_agent_confidence in confidences_neighbour_agents:
            u = u + self.epsilon * (my_confidence-current_neighbour_agent_confidence)

            print('my_confidence = ', my_confidence)
            print('current_neighbour_agent_confidence = ', current_neighbour_agent_confidence)
            print('u = ', u)

        print('u = ', u)

        
        # step 5 : calculate the implicit confidence of my agent
        implicit_confidence = self.CalculateMyImplicitConfidence(target_name)



        # step 6 : calculate the confidence
        my_confidence = my_confidence + u + self.epsilon*(implicit_confidence - my_confidence)

        return my_confidence

    def CalculateMyImplicitConfidence(self, target_name):
        # step 0 : set parameters
        referenced_distance = 500.

        # step 1 : get location of my agent
        my_agent_status = GetMyAgentStatus(self.path_my_agent_status_file, self.file_name_my_agent_status_file)
        my_agent_location = my_agent_status["my_agent_location"]
        print('my_agent_location: ', my_agent_location)


        # step 2 : get all targets' status
        path = "./data/"
        file_name = "all_observed_targets_information.json"

        dict_all_targets_status = GetAllTargetsStatus(path, file_name)

        # step 3 : get the target name
        real_target_name = target_name.split('_')[2]
        print('real_target_name: ', real_target_name)

        # step 4 : get location of the target
        target_location = dict_all_targets_status[real_target_name]['location']
        print('target_location: ', target_location)


        # step 5 : calculate the implicit confidence
        implicit_confidence_squared = 0
        implicit_confidence_squared = implicit_confidence_squared + (my_agent_location['x']-target_location['x'])**2
        implicit_confidence_squared = implicit_confidence_squared + (my_agent_location['y']-target_location['y'])**2
        implicit_confidence_squared = implicit_confidence_squared + (my_agent_location['z']-target_location['z'])**2


        implicit_confidence = implicit_confidence_squared**0.5 / referenced_distance

        print('implicit_confidence: ', implicit_confidence)

        return implicit_confidence


if __name__ == "__main__":
    print('hello')
