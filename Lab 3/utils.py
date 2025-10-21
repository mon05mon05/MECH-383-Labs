import datetime
import os
import re
import serial.tools.list_ports

def create_dir(base_path):
    '''
    Description : 
        Create a new directory to store the results
    Parameters :
        base_path : str
            The base path where the new directory will be created
    Returns :
        dir_name : str
            The name of the new directory
    '''
    # Get the current date in the desired format
    date_str = datetime.datetime.now().strftime("%Y_%m_%d")

    # Get a list of all directories in the base path
    existing_dirs = [d for d in os.listdir(base_path) if os.path.isdir(os.path.join(base_path, d))]

    # Initialize the maximum idx to -1
    max_idx = -1

    # Regex pattern to match directories with the format DATE_idx
    pattern = re.compile(rf"^{date_str}_(\d+)$")

    # Find the maximum idx for the current date
    for dirname in existing_dirs:
        match = pattern.match(dirname)
        if match:
            idx = int(match.group(1))
            if idx > max_idx:
                max_idx = idx

    # Increment the maximum idx to get the new idx
    new_idx = max_idx + 1

    # Construct the new directory name
    dir_name = f"{date_str}_{new_idx}"
    full_path = os.path.join(base_path, dir_name)

    # Create the new directory
    os.makedirs(full_path)
    print(f"Directory created : {full_path}")

    return dir_name, full_path

def find_port(keystring):
    '''
    Description : 
        Find the port of the microcontroller
    Parameters :
        keystring : str
            The keystring that the port description should contain
    Returns :
        port.device : str
            The port of the microcontroller
    '''    
    ports = serial.tools.list_ports.comports()
    for port in ports:
        if keystring in port.description:
            print(port.description)
            return port.device