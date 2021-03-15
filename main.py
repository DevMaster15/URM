import urm_machine
import gestione_file


def main():

    istruction_list = gestione_file.retrive_instructions()
    final_register_list = urm_machine.start_urm(istruction_list) # list of results contained in registers

    # write in a file the result
    with open("results.txt", "w") as fp:
        
        
        for register in final_register_list:
            
            fp.write(str(register) + " ")

        

    print("lista del risultato = " + str(final_register_list))


if __name__ == '__main__':
    main()
