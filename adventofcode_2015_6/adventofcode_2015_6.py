#Import instruction set
f = open("C:\\Users\saidt\Documents\Code\\adventofcode_2015_6\\adventofcode_2015_6.txt", "r")
lighting_instruction_list = f.readlines()
f.close()

#Set up lighting array
new_light_array_status = []
for y in range(1000):
    new_light_array_status.append([])
    for x in range(1000):   
        new_light_array_status[y].append("Off")

light_array_status = new_light_array_status

master_instruction_set = []

#Import Instructions
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

for step in master_instruction_set:
    if step[0] == "On":
        for y in range(int(step[2]),int(step[4]+1)):
            for x in range(step[1],step[3]+1):
                light_array_status[y][x] = "On"

    elif step[0] == "Off":
        for y in range(step[2],step[4]+1):
            for x in range(step[1],step[3]+1):
                light_array_status[y][x] = "Off"

    elif step[0] == "T":
        for y in range(step[2],step[4]+1):
            for x in range(step[1],step[3]+1):
                if light_array_status[y][x] == "Off":
                    light_array_status[y][x] = "On"
                elif light_array_status[y][x] == "On":
                    light_array_status[y][x] = "Off"


lights_on = 0
for d in range(1000):
    for e in range(1000):
        if light_array_status[d][e] == "On":
            lights_on += 1

#print(light_array_status)
print(lights_on)

"""
location_instruction_list = []
for instruction in lighting_instruction_list:
    purged_instruction = instruction.replace("," , " ")
    print(instruction)
    instruction_ref = []
    for i in purged_instruction.split():
        if i.isdigit():
            instruction_ref.append(int(i))
    location_instruction_list.append(instruction_ref)
"""

