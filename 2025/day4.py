import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day4.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

height = len(input_list)
width = len(input_list[0])

total_p1 = 0
total_p2 = 0

removed = []
prev_removed = -1
first_pass = True

while(len(removed) != prev_removed):
    prev_removed = len(removed)
    
    for row in range(height):
        for col in range(width):
            if input_list[row][col] == "@":
                adjacent = 0
                left = col > 0
                right = col < width - 1
                up = row > 0
                down = row < height - 1
                
                # up left
                if up and left:
                    if input_list[row-1][col-1] == "@": adjacent += 1
                # up
                if up:
                    if input_list[row-1][col] == "@": adjacent += 1
                # up right
                if up and right:
                    if input_list[row-1][col+1] == "@": adjacent += 1
                # left
                if left:
                    if input_list[row][col-1] == "@": adjacent += 1
                # right
                if right:
                    if input_list[row][col+1] == "@": adjacent += 1
                # down left
                if down and left:
                    if input_list[row+1][col-1] == "@": adjacent += 1
                # down
                if down:
                    if input_list[row+1][col] == "@": adjacent += 1
                # down right
                if down and right:
                    if input_list[row+1][col+1] == "@": adjacent += 1

                if adjacent < 4:
                    removed.append((row, col))
                    if first_pass:
                        total_p1 += 1

    for (row, col) in removed:
        input_list[row] = input_list[row][:col] + "." + input_list[row][col+1:]

    if first_pass:
        print(total_p1)
        first_pass = False

total_p2 = len(removed)
print(total_p2)