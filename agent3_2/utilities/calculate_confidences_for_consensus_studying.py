# class : calculate_confidence_for_consensus
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

# import utilities of auto logging
from auto_logging import *

class CalculateConfidencesForConsensusStudying:
    def __init__(
        self, 
        path_my_agent_status_file, 
        file_name_my_agent_status_file, 
        neighbour_agents_confidences_to_all_targets, 
        path_all_observed_targets_information_file, 
        file_name_all_observed_targets_information_file):

        self.path_my_agent_status_file      = path_my_agent_status_file
        self.file_name_my_agent_status_file = file_name_my_agent_status_file

        self.neighbour_agents_confidences_to_all_targets = neighbour_agents_confidences_to_all_targets

        self.path_all_observed_targets_information_file = path_all_observed_targets_information_file
        self.file_name_all_observed_targets_information_file = file_name_all_observed_targets_information_file


        # get my agent's previous confidence, which was written in the file, file_name_my_agent_status_file
        self.my_confidences_to_all_targets = GetMyConfidencesToAllTargets(
            path_my_agent_status_file, file_name_my_agent_status_file)

        # set parameters
        self.epsilon = 1.

        # set the confidences
        self.dict_my_agent_confidences = {}

        # set my auto logging
        self.my_auto_logging = 0
        self.is_my_auto_logging_set = False


        # debug
        #print("class CalculateConfidences: ")
        #print('path_my_agent_status_file, file_name_my_agent_status_file',self.path_my_agent_status_file,file_name_my_agent_status_file)
        #print('my_confidences_to_all_targets', self.my_confidences_to_all_targets)
        #print('neighbour_agents_confidences_to_all_targets', self.neighbour_agents_confidences_to_all_targets)
        #print('path_all_observed_targets_information_file, file_name_all_observed_targets_information_file', self.path_all_observed_targets_information_file , self.file_name_all_observed_targets_information_file)
        # !debug

        return

    def DoCalculation(self):
        # step 1 : get target names
        for target_name in self.my_confidences_to_all_targets:
            my_confidence = self.DoCalculationAccordingToTarget(target_name)

            # debug
            #print('target_name: ', target_name, ', my_confidence = ', my_confidence)
            # !debug

            # step 2 : store the confidence into the self.dict_my_agent_confidences 
            self.dict_my_agent_confidences[target_name] = my_confidence

            # logging starts...
            if self.is_my_auto_logging_set:
                my_logging_line = target_name + ' : ' + str(self.dict_my_agent_confidences[target_name]) + '\n'
                self.my_auto_logging.DoLoggingString("\nclass CalculateConfidencesForConsensusStudying, , step 1 : get target names, step 2 : store the confidence into the self.dict_my_agent_confidences\n")
                self.my_auto_logging.DoLoggingString(my_logging_line)

                my_logging_line = 'DoCalculation Ends' + '\n'
                my_logging_line += '----' + '\n'
                my_logging_line += '------------' + '\n'
                my_logging_line += '\n'
                self.my_auto_logging.DoLoggingString(my_logging_line)
            # logging ends.

        # debug
        #print('----dict_my_agent_confidences', self.dict_my_agent_confidences)

        return self.dict_my_agent_confidences

    def DoCalculationAccordingToTarget(self, target_name):
        # step 0 : show target_name
        # debug
        #print('DoCalculationAccordingToTarget,  step 0 : show target_name, ', target_name)
        # !debug
    
        # step 1 : initiate parameter u
        u = 0

        # step 2 : get my previous confidence
        my_previous_confidence = self.my_confidences_to_all_targets[target_name]

        # logging starts...
        if self.is_my_auto_logging_set:
            my_logging_line = 'my_previous_confidence : ' + str(my_previous_confidence) + '\n'
            self.my_auto_logging.DoLoggingString("\nclass CalculateConfidencesForConsensusStudying, DoCalculationAccordingToTarget, target_name: "+target_name+"\n")
            self.my_auto_logging.DoLoggingString(my_logging_line)
        # logging ends.

        # step 3 : get  confidence of the neighbour agents
        confidences_neighbour_agents = self.neighbour_agents_confidences_to_all_targets[target_name]

        # logging starts...
        if self.is_my_auto_logging_set:

            my_logging_line = 'confidences_neighbour_agents : '
            for element in confidences_neighbour_agents: 
                my_logging_line = my_logging_line + str(element) + ', '
            my_logging_line += '\n'

            self.my_auto_logging.DoLoggingString("\nclass CalculateConfidencesForConsensusStudying, DoCalculationAccordingToTarget, step 3 : get  confidence of the neighbour agents\n")
            self.my_auto_logging.DoLoggingString(my_logging_line)
        # logging ends.

        # step 4 : do calculate
        for current_neighbour_agent_confidence in confidences_neighbour_agents:
            u = u + self.epsilon * (current_neighbour_agent_confidence - my_previous_confidence)

        # logging starts...
        if self.is_my_auto_logging_set:
            my_logging_line = 'u : ' + str(u) + '\n'
            self.my_auto_logging.DoLoggingString("\nclass CalculateConfidencesForConsensusStudying, DoCalculationAccordingToTarget, step 4 : do calculate\n")
            self.my_auto_logging.DoLoggingString(my_logging_line)
        # logging ends.

        # step 5 : calculate the implicit confidence of my agent
        #implicit_confidence = self.CalculateMyImplicitConfidence(target_name)


        # step 6 : calculate the confidence
        #my_confidence = my_previous_confidence + u + self.epsilon*(implicit_confidence - my_previous_confidence)
        my_confidence = my_previous_confidence + u

        # logging starts...
        if self.is_my_auto_logging_set:
            my_logging_line = 'my_confidence(' + str(my_confidence) + ')'
            my_logging_line = my_logging_line + ' = my_previous_confidence(' + str(my_previous_confidence) + ')'
            my_logging_line = my_logging_line + ' + u(' + str(u) + ')'
            self.my_auto_logging.DoLoggingString("\nclass CalculateConfidencesForConsensusStudying, DoCalculationAccordingToTarget, step 6 : calculate the confidence\n")
            self.my_auto_logging.DoLoggingString(my_logging_line)
        # logging ends.

        return my_confidence

    def CalculateMyImplicitConfidence(self, target_name):
        # step 0 : set parameters
        referenced_distance = 1000.

        # step 1 : get location of my agent
        my_agent_status = GetMyAgentStatus(self.path_my_agent_status_file, self.file_name_my_agent_status_file)
        my_agent_location = my_agent_status["my_agent_location"]


        # step 2 : get all targets' status
        path = "./data/"
        file_name = "all_observed_targets_information.json"

        dict_all_targets_status = GetAllTargetsStatus(path, file_name)

        # step 3 : get the target name
        real_target_name = target_name.split('_')[2]

        # step 4 : get location of the target
        # step 4.1 : if status of the target did not exist in the file, notice shold be made 
        if real_target_name not in dict_all_targets_status:
            print("!!!! NOTICE !!!!: Status of the target did not exist in the file!")
            return 0

        # step 4.2 : get status of the target
        target_location = dict_all_targets_status[real_target_name]['location']

        # step 5 : calculate the implicit confidence
        implicit_confidence_squared = 0
        implicit_confidence_squared = implicit_confidence_squared + (my_agent_location['x']-target_location['x'])**2
        implicit_confidence_squared = implicit_confidence_squared + (my_agent_location['y']-target_location['y'])**2
        implicit_confidence_squared = implicit_confidence_squared + (my_agent_location['z']-target_location['z'])**2

        # wrong
        #implicit_confidence = implicit_confidence_squared**0.5 / referenced_distance
        # !wrong

        implicit_confidence = referenced_distance / implicit_confidence_squared**0.5 

        return implicit_confidence


    def GetMyConfidences(self):
        return

    def SetMyAutoLogging(self, my_auto_logging):
        self.my_auto_logging = my_auto_logging
        self.is_my_auto_logging_set = True
        return


if __name__ == "__main__":
    print('hello')
