# URM's function

# function that sets register value to 0
def zero():
    register_value = 0
    return register_value

# function that increments register value by 1
def incr(register_value):
    register_value += 1
    return register_value


# paste value of register_A in register_B
def proj(register_1, register_2):
    register_2 = register_1
    return register_2


# function that "jump" to index indicated in jump
def jump(reg1, reg2, jump, program_counter):

    # if reg1 == reg2 jump
    if check_register_equality(reg1, reg2):
        if jump >= 255:
            return jump
        else:
            new_program_counter = jump
            return new_program_counter
    else:
        # if reg1 != reg2 increment simply program counter
        new_program_counter = program_counter + 1
        return new_program_counter


def check_register_equality(reg1, reg2):

    if reg1 == reg2:
        return True
    else:
        return False