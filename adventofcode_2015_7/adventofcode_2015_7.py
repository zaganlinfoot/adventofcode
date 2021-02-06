#Import instruction set
f = open("C:\\Users\saidt\Documents\Code\\adventofcode_2015_7\\adventofcode_2015_7part2.txt", "r")
wire_id_logic = f.readlines()
f.close()

#Set up and populate wire id dictionary
wire_id_dictionary = {}
for line in wire_id_logic:
    wire_logic_list = line.split()
    wire_id_dictionary[wire_logic_list[-1]] = wire_logic_list[:-2]

solved_dictionary = {}

#Function to check if single value is an integer(return binary string) or wire id(call recursive check)
def single_item_check(dictionary_output_value):
        if dictionary_output_value in solved_dictionary:
            return solved_dictionary[dictionary_output_value]
        elif dictionary_output_value.isdigit():
            return format(int(dictionary_output_value), "016b")
            
        else:
            solved_value = recursive_define(dictionary_output_value)
            solved_dictionary[dictionary_output_value] = solved_value
            return solved_value

#Function to preform NOT shift is list length is 2
def not_function(dictionary_output):
    #Check if the argument in the not fucntion is a integer or a wire id
    not_check_string = single_item_check(dictionary_output[1])
    #Set up the NOT shifted string
    output_list = str()
    #Perform the NOT shift
    for i in not_check_string:
        if i == "0": 
            output_list = output_list + "1"
        elif i == "1":
            output_list = output_list + "0"
        #Return the NOT shifted string
    return output_list

#Function to determine which shift to apply AND OR LSHIFT RSHIFT if list lenght is 3 
def len_three_func_check(dictionary_output_list):
    if "AND" in dictionary_output_list:
        return and_function(dictionary_output_list)
    elif "OR" in dictionary_output_list:
        return or_function(dictionary_output_list)
    elif "LSHIFT" in dictionary_output_list:
        return lshift_function(dictionary_output_list)
    elif "RSHIFT" in dictionary_output_list:
        return rshift_function(dictionary_output_list)

#Function to perform AND operation
def and_function(dictionary_output_list):
    #Check if the argument x is a integer or a wire id
    x = single_item_check(dictionary_output_list[0])
    #Check if the argument y is a integer or a wire id
    y = single_item_check(dictionary_output_list[2])
    #Set up the AND shifted string and lists to operate on
    x_list = []
    x_list[:0] = x
    y_list = []
    y_list[:0] = y
    output_list = str()
    #Perform the AND shift
    for i in range(len(x_list)):
        if x_list[i] == "1": 
            if y_list[i] == "1":
                output_list = output_list + "1"
            else:
                output_list = output_list + "0"
        else:
            output_list = output_list + "0"
    #Return the AND binary string
    return output_list

#Function to perform OR operation
def or_function(dictionary_output_list):
    #Check if the argument x is a integer or a wire id
    x = single_item_check(dictionary_output_list[0])
    #Check if the argument y is a integer or a wire id
    y = single_item_check(dictionary_output_list[2])
    #Set up the AND shifted string and lists to operate on
    x_list = []
    x_list[:0] = x
    y_list = []
    y_list[:0] = y
    output_list = str()
    #Perform the OR shift
    for i in range(len(x_list)):
        if x_list[i] == "0": 
            if y_list[i] == "0":
                output_list = output_list + "0"
            else:
                output_list = output_list + "1"
        else:
            output_list = output_list + "1"
    #Return the OR binary string
    return output_list

#Function to perform LSHIFT operation
def lshift_function(dictionary_output_list):
    #Check if the argument x is a integer or a wire id
    x = single_item_check(dictionary_output_list[0])
    bit_shift_list = x + (int(dictionary_output_list[2]) * "0")
    output_list = bit_shift_list[-16:]
    return output_list

#Function to perform RSHIFT operation
def rshift_function(dictionary_output_list):
    #Check if the argument x is a integer or a wire id
    x = single_item_check(dictionary_output_list[0])
    bit_shift_list = (int(dictionary_output_list[2]) * "0") + x
    output_list = bit_shift_list[:16]
    return output_list

#Set up recursive check funtion
def recursive_define(dictionary_key_letter):
    dictionary_output_list = wire_id_dictionary[dictionary_key_letter]
    #If length is 1 call the single_item_check function to return the binary string or call the recursion check on the one wire id
    if len(dictionary_output_list) == 1:
        return single_item_check(dictionary_output_list[0])
    #If length is 2 call the NOT shift function as not_function
    elif len(dictionary_output_list) == 2:
        return not_function(dictionary_output_list)
    #If length is 3 call a function to determine which shift to apply AND OR LSHIFT RSHIFT
    elif len(dictionary_output_list) == 3:
        return len_three_func_check(dictionary_output_list)

#Function to convert binary output string to integer
def convert_bin_to_int(string_input):
    binary_list=[]
    binary_list[:0] = string_input
    integer_sum = (32768*int(binary_list[0])) + (16384*int(binary_list[1])) + (8192*int(binary_list[2])) + (4096*int(binary_list[3])) + (2048*int(binary_list[4])) + (1024*int(binary_list[5])) + (512*int(binary_list[6])) + (256*int(binary_list[7])) + (128*int(binary_list[8])) + (64*int(binary_list[9])) + (32*int(binary_list[10])) + (16*int(binary_list[11])) + (8*int(binary_list[12])) + (4*int(binary_list[13])) + (2*int(binary_list[14])) + (1*int(binary_list[15])) 
    return integer_sum

#dictionary_key_letter = "x"
#print(wire_id_dictionary["a"])
#print(wire_id_dictionary)
#print(recursive_define("a"))
#print(and_function("x"))
print(convert_bin_to_int(recursive_define("a")))

# c = a | b
# c = a & b
# c = (~b) & 65535
# c = (a << 2) & 65535
# c = a >> 2