from itertools import groupby

def lookandsay(input_string):
    inputstring_group_list = [list(g) for k, g in groupby(input_string)]
    lookandsay_new = str()
    for i in range(len(inputstring_group_list)):
        number = inputstring_group_list[i][0]
        count = len(inputstring_group_list[i])
        lookandsay_new = lookandsay_new + str(count) + str(number) 
    return lookandsay_new

finalstring = "1113122113"
for i in range(40):
    finalstring = lookandsay(finalstring)


print(len(finalstring))

"""
def lookandsay (string_input, num_of_loops):
    current_string = []
    current_string[:0] = string_input
    current_num_in_string = 0
    current_num_count = 0
    for i in range(num_of_loops):
        for i in range(len(current_string)):
            if current_string[i] == current_string[i+1]:
                current_num_in_string = current_string[i]
"""
