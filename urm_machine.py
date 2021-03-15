from URM import *


def start_urm(instruction_list):


    program_counter = 0    # it "counts" instructions, and indicates what instruction should be execute at a time
    registers_list = [0] * 256  # list that represents all 256 registers, initializing them to 0
    last_register_used_index = 0
    while program_counter <= len(instruction_list):  # while program counter is a value lower than the len(list_instruction) means that there are instruction to execute

        instruction_code = instruction_list[program_counter][0]  # it reprensents URM's function

        if instruction_code == 0:   # if instruction_code is 0, execute zero()

            register_index = instruction_list[program_counter][1]

            registers_list[register_index] = zero()
            program_counter += 1

        elif instruction_code == 1:  # if instruction_code is 1, execute incr(x)
            register_index = instruction_list[program_counter][1]
            
            registers_list[register_index] = incr(registers_list[register_index])
            program_counter += 1

        elif instruction_code == 2:    # if instruction_code is 2, execute proj(x,y)

            register_index_1 = instruction_list[program_counter][1]    # first index register
            register_index_2 = instruction_list[program_counter][2]    # second index register

            register_1 = registers_list[register_index_1]  # first register
            register_2 = registers_list[register_index_2]  # second register

            # value of the first register is copy in the second register
            registers_list[register_index_2] = proj(register_1, register_2)

            program_counter += 1

        elif instruction_code == 3:    # if instruction_code is 3, execute jump(x,y,z)

            register_index_1 = instruction_list[program_counter][1]  # first index register
            register_index_2 = instruction_list[program_counter][2]  # second index register

            register_1 = registers_list[register_index_1]  # first register
            register_2 = registers_list[register_index_2]  # second register

            jump_value = instruction_list[program_counter][3]

            program_counter = jump(register_1, register_2, jump_value, program_counter)

        else:
            print("ERRORE")

    return registers_list  # when program counter is greater than len(instruction_list) return list of registers
