f = open("C:\\Users\saidt\Documents\Code\\adventofcode_2015_5\\adventofcode_2015_5.txt", "r")
naughty_or_nice_text_list = f.readlines()
f.close()

def double_letter_check(string_to_check):
    for position in range(len(string_to_check)-1):
        if string_to_check[position] == string_to_check[position+1]:
            return True

def double_letter_spaced_check(string_to_check):
    for position in range(len(string_to_check)-2):
        if string_to_check[position] == string_to_check[position+2]:
            return True

def specific_letter_count(string_to_check):
    number_of_specific_letters = 0
    specific_letters = ["a", "e", "i", "o", "u"]
    for position in range(len(string_to_check)):
        for i in specific_letters:
            if string_to_check[position] == i:
                number_of_specific_letters +=1
    if number_of_specific_letters >= 3:
        return True

def specific_combination_count(string_to_check):
    number_of_specific_combinations = 0
    specific_combinations = ["ab", "cd", "pq", "xy"]
    for position in range(len(string_to_check)-1):
        for i in specific_combinations:
            if string_to_check[position:position+2] == i:
                number_of_specific_combinations +=1
    if number_of_specific_combinations >= 1:
        return True

def two_letters_twice(string_to_check):
    number_of_two_combinations = 0
    for position in range(len(string_to_check)-1):
        check_pair = string_to_check[position:position+2]
        remaining_string_to_check = string_to_check[position+2:]
        if check_pair in remaining_string_to_check:
            number_of_two_combinations +=1
    if number_of_two_combinations >= 1:
        return True

def count_nice_strings(list_to_check):
    nice_strings = 0
    for naughty_or_nice in list_to_check:
        if double_letter_check(naughty_or_nice) == True and specific_letter_count(naughty_or_nice) == True and specific_combination_count(naughty_or_nice) != True:
            nice_strings +=1
    return nice_strings

def count_nice_strings_part_two(list_to_check):
    nice_strings = 0
    for naughty_or_nice in list_to_check:
        if two_letters_twice(naughty_or_nice) == True and double_letter_spaced_check(naughty_or_nice) == True:
            nice_strings +=1
    return nice_strings

print(count_nice_strings(naughty_or_nice_text_list))
print(count_nice_strings_part_two(naughty_or_nice_text_list))