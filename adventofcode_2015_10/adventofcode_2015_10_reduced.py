from itertools import groupby

def lookandsay(input_string):
    inputstring_group_list = [list(g) for k, g in groupby(input_string)]
    lookandsay_new = str()
    for i in range(len(inputstring_group_list)):
        number = inputstring_group_list[i][0]
        count = len(inputstring_group_list[i])
        lookandsay_new += str(count) + str(number) 
    return lookandsay_new

def lookandsay_string(input_string):
    working_string = str(input_string) + "x"
    compare_number = working_string[0]
    working_count = 1
    output_string = str()
    for i in working_string[-(len(working_string)-1):]:
        if i == compare_number:
            working_count += 1
        else:
            output_string += str(working_count) + str(compare_number)
            compare_number = i
            working_count = 1
    return output_string

def lookandsay_output(input_string, number_of_cycles):
    finalstring = str(input_string)
    for i in range(number_of_cycles):
        finalstring = lookandsay(finalstring)
    return finalstring

def lookandsay_string_output(input_string, number_of_cycles):
    finalstring = str(input_string)
    for i in range(number_of_cycles):
        finalstring = lookandsay_string(finalstring)
    return finalstring


print(len(lookandsay_output(1113122113, 50)))
#print(len(lookandsay_string_output(1113122113, 50)))

"""
calculated_length = (360154 * (1.3035772690342296 **10))
print(calculated_length)
"""