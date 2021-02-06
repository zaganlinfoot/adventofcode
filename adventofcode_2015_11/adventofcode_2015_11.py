def next_pass(pass_string):
  pass_list = list(pass_string)
  pass_list.reverse()
  for i in range(len(pass_list)):
    if pass_list[i] == 'z':
      pass_list[i] = 'a'
    else:
      pass_list[i] = chr(ord(pass_list[i]) + 1)
      pass_list.reverse()
      next_pass = "".join(pass_list)
      return next_pass

def increasing_straight(pass_string):
    for position in range(len(pass_string)-2):
        if ord(pass_string[position]) == ord(pass_string[position+1])-1 == ord(pass_string[position+2])-2:
            return True

"""
def disallowed_letters(pass_string):
    number_of_disallowed_letters = 0
    specific_letters = ["i", "o", "l"]
    for position in range(len(pass_string)):
        for i in specific_letters:
            if pass_string[position] == i:
                number_of_disallowed_letters +=1
    if number_of_disallowed_letters == 0:
        return True
    else: 
        return False
"""

def disallowed_letters(pass_string):
    if pass_string.find("i") == -1 and pass_string.find("o") == -1 and pass_string.find("l") == -1:
        return True
    else: 
        return False

def double_letter_check(pass_string):
    iter_pass_string = list(pass_string)
    paired_letter_list = []
    for position in range(len(iter_pass_string)-1):
        if iter_pass_string[position] == iter_pass_string[position+1]:
            paired_letter_list.append(iter_pass_string[position])
    if len(paired_letter_list) >= 2:
        for position in range(len(paired_letter_list)-1):
            if paired_letter_list[position] != paired_letter_list[position+1]:
                return True

def next_valid_password(pass_string):
    next_password = next_pass(pass_string)
    while (increasing_straight(next_password) and disallowed_letters(next_password) and double_letter_check(next_password)) != True:
        next_password = next_pass(next_password)
    return next_password

print(next_valid_password("hxbxxzaa"))