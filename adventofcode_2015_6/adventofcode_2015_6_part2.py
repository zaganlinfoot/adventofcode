#Import instruction set
f = open("C:\\Users\saidt\Documents\Code\\adventofcode_2015_6\\adventofcode_2015_6.txt", "r")
lighting_instruction_list = f.readlines()
f.close()

#Set up lighting array
new_light_array_status = []
for y in range(1000):
    new_light_array_status.append([])
    for x in range(1000):   
        new_light_array_status[y].append(0)

#print(new_light_array_status[3])

light_array_status = new_light_array_status

#Import and parse instructions in to master instruction set
master_instruction_set = []
for instruction in lighting_instruction_list:
    switch_instruction_list = []
    toggle = "toggle"
    turn_on = "turn on"
    turn_off = "turn off"
    if toggle in instruction:
        switch_instruction_list.append("T")
    elif turn_on in instruction:
        switch_instruction_list.append("On")
    elif turn_off in instruction:
        switch_instruction_list.append("Off")
    purged_instruction = instruction.replace("," , " ")
    for i in purged_instruction.split():
        if i.isdigit():
            switch_instruction_list.append(int(i))
    master_instruction_set.append(switch_instruction_list)

#Turn lights on and off in light_array_status
for step in master_instruction_set:
    if step[0] == "On":
        for y in range(int(step[2]),int(step[4]+1)):
            for x in range(step[1],step[3]+1):
                light_array_status[y][x] += 1

    elif step[0] == "Off":
        for y in range(step[2],step[4]+1):
            for x in range(step[1],step[3]+1):
                if light_array_status[y][x] > 0:
                    light_array_status[y][x] -= 1

    elif step[0] == "T":
        for y in range(step[2],step[4]+1):
            for x in range(step[1],step[3]+1):
                light_array_status[y][x] +=2

#Sum total lights on
by_row = []
for d in range(1000):
    row = light_array_status[d]
    sum_of_row = sum(row)
    by_row.append(sum_of_row)

total_light_power = sum(by_row)

print(total_light_power)