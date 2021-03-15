# method that converts byte to int value
import sys


def convertToInt(byte):

    int_value = int.from_bytes(byte, byteorder='big')
    return int_value


def retrive_instructions():
    # start program
    list_instruction = []
    final_list = []

    name = sys.argv[1]

    # initialize file descriptor f
    with open(name, "rb") as f:
        byte = f.read(1)  # read 1 bytes at a time
        counter = 0
        
        while byte:  # while byte is not null
            byte = convertToInt(byte)

            # create list of instruction -> [[byte1, byte2, byte3, byte4], [...], ...]
            list_instruction.insert(counter, byte)

            counter += 1

            # count if there are 4 "bytes" in a sublist
            # if yes, append that list to the final_list
            if counter > 3:
                final_list.append(list_instruction)
                list_instruction = []
                counter = 0

            byte = f.read(1)

    return final_list