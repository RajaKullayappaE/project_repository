import json


def read_data(file):
    """
    Reads the data from a file
    Args:
        file: File name or path
    """
    with open(file, "r") as file_obj:
        data = file_obj.read()
    return json.loads(data)