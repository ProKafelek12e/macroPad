import json

# Specify the path to your JSON file
def read(json_file_path):

    with open(json_file_path, "r") as json_file:

        data = json.load(json_file)
    return(data)
def write(json_file_path,dataToWrite):

    with open(json_file_path, "w") as json_file:
        # Write the data to the JSON file
        json.dump(dataToWrite, json_file)

    print("Data has been written to", json_file_path)