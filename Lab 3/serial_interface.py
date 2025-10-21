# Author : Wilfred Mason
# Last update : 2024-07-23
# Description : This file contains the serial interface class that is used to communicate with the arduino board


import serial
import time
import utils
import os

def main():
    try:
        log = None
        ser = None

        # Do not modify the following variables
        PORT_KEY = "USB Serial Device"
        BAUD_RATE = 9600
        # Get the current working directory
        current_directory = os.getcwd()

        # Set the base_path to the 'results' subfolder within the current directory
        BASE_PATH = os.path.join(current_directory, "results")

        # Create the 'results' directory if it doesn't exist
        os.makedirs(BASE_PATH, exist_ok=True)

        print(BASE_PATH)

        # BASE_PATH = "results"

        ##### Serial setup #####
        # Find MCU port
        MCU_port = utils.find_port(keystring=PORT_KEY)
        if MCU_port is None:
            raise Exception("Microcontroller not found")
        # Open serial port
        ser = serial.Serial(port=MCU_port, baudrate=BAUD_RATE) 
        if ser.is_open:
            print("Serial port open")
 
        ##### Create Directory & File to Save Results #####
        _, full_path = utils.create_dir(base_path=BASE_PATH)
        print(f"Directory created : {full_path}")
        # Create txt file to save results
        file_name = "log.txt"
        file_path = os.path.join(full_path, file_name)
        log = open(file_path, "w")

        ##### Main loop #####
        while True:
            if ser.in_waiting > 0:
                # Read data from MCU
                data = ser.readline().decode("utf-8").strip()
                # Get current time
                current_time = time.time()
                # Print current time and angle
                print(f"Time-stamp: {current_time:10.5f} | Data: {data}")
                # Save data to file
                log.write(f"{current_time},{data}\n")
    
    except Exception as e:
        print(f"Error during initialization : {e}")
    except KeyboardInterrupt:
        print("Serial interface stopped")
    finally:
        if ser is not None:
            ser.close()
            print("Serial port closed")
        if log is not None:
            log.close()
            print("File closed")

    return None


if __name__ == "__main__":
    main()