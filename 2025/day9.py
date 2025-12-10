import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day9.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

red_squares = []
for curr_square in input_list:
    temp_light = curr_square.split(",")
    ts_x = int(temp_light[0])
    ts_y = int(temp_light[1])

    red_squares.append((ts_x, ts_y))

area = []
for row in range(len(red_squares)):
    for col in range(row+1, len(red_squares)):
        square1 = red_squares[row]
        square2 = red_squares[col]
        curr_area = (abs(square1[0] - square2[0]) + 1) * (abs(square1[1] - square2[1]) + 1)
        area.append((curr_area, (row, col)))
area.sort(reverse=True)

(total_p1, (p1_1, p1_2)) = area[0]

print(total_p1)