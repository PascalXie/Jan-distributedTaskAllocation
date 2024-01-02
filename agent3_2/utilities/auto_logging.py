# class : auto logging
import json

# preparation for importing utilities
import sys
sys.path.append("../utilities")

class AutoLogging:
    def __init__(self, path, file_name):
        self.path_ = path
        self.file_name_ = file_name
        return

    def DoLoggingfloat(self, number):
        line = str(number)
        with open(self.path_+self.file_name_, "a", encoding="utf-8") as write_file:
            write_file.write(line)
            write_file.close()

    def DoLoggingString(self, line):
        with open(self.path_+self.file_name_, "a", encoding="utf-8") as write_file:
            write_file.write(line)
            write_file.close()

    def DoLoggingDictionary(self, line_dict):

        line = json.dumps(line_dict, sort_keys=True, indent=4)
        line += "\n"

        with open(self.path_+self.file_name_, "a", encoding="utf-8") as write_file:
            write_file.write(line)
            write_file.close()

        return

if __name__ == "__main__":
    print('hello')

    path = "../log/"
    file_name = "log_test1.log"
    my_auto_logging = AutoLogging(path, file_name)
    my_auto_logging.DoLoggingString("hello\n")
