file = open("day1.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

position_p1 = 50
zero_count_p1 = 0

for curr_move in input_list:
    direction = 0
    if curr_move != "":
        if curr_move[0] == "R":
            direction = 1
        else:
            direction = -1
            
        amount = int(curr_move[1:]) * direction

        position_p1 = (position_p1 + amount) % 100
        if position_p1 == 0:
            zero_count_p1 += 1

print(zero_count_p1)

position_p2 = 50
zero_count_p2 = 0

for curr_move in input_list:
    direction = 0
    if curr_move != "":
        if curr_move[0] == "R":
            direction = 1
        else:
            direction = -1
            
        amount = int(curr_move[1:]) * direction
        
        for i in range(0, amount, direction):
            position_p2 = (position_p2 + direction) % 100

            if position_p2 == 0:
                zero_count_p2 += 1

print(zero_count_p2)
