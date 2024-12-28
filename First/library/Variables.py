import json

class Variables:
    def __init__(self,variable_name):
        self.path = r"D:\Programming\Python\College\First\config\config.cfg"
        self.name = variable_name

    def get_variable(self):
        with open(self.path) as file:
            file_content = json.loads(file.read())
            return file_content[self.name]
        

