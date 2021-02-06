#Import instruction set
f = open("C:\\Users\saidt\Documents\Code\\adventofcode_2015_8\\adventofcode_2015_8.txt", "r")
escaped_strings_file = f.readlines()
f.close()

#Import standard file to decode the literal input
import codecs

#Determine the literal (in memory) and decoded (as shown on screen) lengths
literal_string_length_list = []
decoded_string_length_list = []
for i in escaped_strings_file:
    #Strip the line returns
    string_literal = i.strip("\n")
    #Determine decoded string from imported file
    string_decoded = codecs.decode(string_literal, "unicode_escape")
    #Determine the literal length of the string and append to the list
    length_of_string_literal = len(string_literal)
    literal_string_length_list.append(length_of_string_literal)
    #Determine decoded length of the string and append to the list
    length_of_string_decoded = len(string_decoded)-2
    decoded_string_length_list.append(length_of_string_decoded)

#Part two count logic
part_two_count = 0
for each_string in escaped_strings_file:
    literal_string_list = []
    #Strip the line return
    each_string_stripped = each_string.strip("\n")
    #Build a list of the characters in the literal string
    for letters in each_string_stripped:
        literal_string_list.append(letters)
    #Count each character, count two for " and \ characters
    for position in literal_string_list:
        if position == "\"":
            part_two_count += 2
        elif position == "\\":
            part_two_count += 2
        else:
            part_two_count += 1
    #Add two for the "" needed for the new string
    part_two_count += 2

total_literal = sum(literal_string_length_list)
total_decoded = sum(decoded_string_length_list)
literal_minus_decoded = total_literal - total_decoded
part_two_answer = part_two_count - total_literal

print("Total literal is,", total_literal)
print("Part_two_count is,", part_two_count)
print("Part two answer is,", part_two_answer)
#print(total_decoded)
#print(literal_minus_decoded)