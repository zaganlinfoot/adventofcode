#Import test file
f = open("C:\\Users\\saidt\\Documents\\Code\\adventofcode_2015_12\\adventofcode_2015_12.txt", "r")
json_input = f.read()
f.close()

number_read_from_text = str()
numbers_from_json_input = []
for x in json_input:
    if x.isdigit() or x == "-":
        number_read_from_text += x
    elif len(number_read_from_text) > 0:
        numbers_from_json_input.append(int(number_read_from_text))
        number_read_from_text = str()
    else:
        continue

    #[int(x) for x in json_input if x.isdigit()]

print(json_input.split('{')[4])