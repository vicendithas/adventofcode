import copy

import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day12.txt", "r")
input_string = file.read()
map_list = input_string.split("\n")

#remove the blank line at the end
map_list.pop()

height = len(map_list)
width = len(map_list[0])

visitedA = []
for y in range(height):
    curr_line = []
    for x in range(width):
        curr_line.append(False)
    visitedA.append(curr_line)

visitedP = copy.deepcopy(visitedA)

curr_region = []

def getArea(y, x, crop):
    #if the square is out of bounds, return
    if (y < 0) or (y > height - 1) or (x < 0) or (x > width - 1): return 0

    #if we've already visited this square, return
    if visitedA[y][x]: return 0

    #if the new crop doesn't equal the passed crop, return
    if map_list[y][x] != crop: return 0

    #we are now at a point where we want to process the current square
    visitedA[y][x] = True
    curr_region.append([y, x])

    return 1 + getArea(y-1, x, crop) + getArea(y+1, x, crop) + getArea(y, x-1, crop) + getArea(y, x+1, crop)

def getPerimSides():
    perim = 0
    for coord in curr_region:
        y = coord[0]
        x = coord[1]
        curr_crop = map_list[y][x]
        curr_perim = 4

        #up
        if (y > 0) and map_list[y-1][x] == curr_crop: perim -= 1

        #down
        if (y < height - 1) and map_list[y+1][x] == curr_crop: perim -= 1

        #left
        if (x > 0) and map_list[y][x-1] == curr_crop: perim -= 1

        #right
        if (x < width - 1) and map_list[y][x+1] == curr_crop: perim -= 1

        perim += curr_perim
        
    return (perim, 0)

total = 0
for y in range(height):
    for x in range(width):
        if visitedA[y][x]: continue

        curr_region = []
        area = getArea(y, x, map_list[y][x])
        (perim, sides) = getPerimSides()
        total += area * perim
        
print(total)
    
