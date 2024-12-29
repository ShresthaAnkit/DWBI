import json

class Variables:
    @staticmethod
    def get_variable(variable_name):
        try:
            path = r"D:\Programming\Python\College\First\config\config.cfg"
            with open(path) as file:
                file_content = json.loads(file.read())
                return file_content[variable_name]
        except Exception as e:
            print(f"[ERROR]: {e}")


