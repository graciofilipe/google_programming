def scan_for_outter_parts(string):
    open_positions = []
    close_positions = []
    number_of_reps = []
    string_len = len(string)
    balance = 0
    for i in range(string_len):

        if string[i] =='[' and balance==0:
            open_positions.append(i)
            balance += 1
        elif string[i] =='[' and balance != 0:
            balance += 1
        elif string[i] ==']' and balance==1:
            close_positions.append(i)
            balance -= 1
        elif string[i] ==']' and balance!=1:
            balance -= 1
    return (open_positions, close_positions)

def return_reps(string, starting_pos):
    number_of_reps = []
    for i in starting_pos:
        j = i - 1
        s1 = string[j]
        cont = True
        while cont:
            if string[j - 1] in ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']:
                s1 += string[j - 1]
                j -= 1
            else:
                cont = False
        s1 = s1[::-1]
        number_of_reps.append(s1)

    return number_of_reps


def decompress(input_string):
    pass
