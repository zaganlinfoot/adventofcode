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
    if pass_string.find("i") == -1 and pass_string.find("o") == -1 and pass_string.find("l") == -1:
        return True
    else: 
        return False
"""

def disallowed_letters(pass_string):
    bad_letters = ['i', 'o', 'u']
    return not any(x in pass_string for x in bad_letters)

def double_letter_check(pass_string):
    double_letter_count = 0
    i = 0
    while i < len(pass_string)-1:
        if pass_string[i] == pass_string[i+1]:
            double_letter_count += 1
            i += 2
        else: 
            i += 1
    if double_letter_count >= 2:
        return True

def next_valid_password(pass_string):
    next_password = next_pass(pass_string)
    while (increasing_straight(next_password) and disallowed_letters(next_password) and double_letter_check(next_password)) != True:
        next_password = next_pass(next_password)
    return next_password

print(next_valid_password("hxbxxyzz"))