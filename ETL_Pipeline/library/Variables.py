import json

class Variables:
    @staticmethod
    def get_variable(variable_name):
        path = r"D:\Programming\Python\College\ETL_Pipeline\config\config.cfg"
        try:
            with open(path) as file:
                file_content = json.loads(file.read())
                return file_content[variable_name]
        except FileNotFoundError:
            raise FileNotFoundError(f"Configuration file not found at {path}.")
        except json.JSONDecodeError as e:
            raise ValueError(f"Error parsing JSON in configuration file: {e}")
        except Exception as e:
            raise Exception(f"An unexpected error occurred: {e}")


