input_string = 311311222113

working_string = str(input_string) + "x"
compare_number = working_string[0]
print(compare_number)
working_count = 1
output_string = str()
for i in working_string[-(len(working_string)-1):]:
    print(i)
    if i == compare_number:
        working_count += 1
    else:
        output_string = output_string + str(working_count) + str(compare_number)
        compare_number = i
        working_count = 1
print(output_string)
