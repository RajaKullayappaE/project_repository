from read_file import read_data
from frequency import compute_frequency


def project():
    file_path = "input/input_data.json"
    text = read_data(file_path)["text"]
    result = compute_frequency(text)
    print(result)

project()