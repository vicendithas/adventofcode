import os
script_path = os.path.abspath(__file__)
script_dir = os.path.dirname(script_path)

file = open(script_dir + "/input/day8.txt", "r")
input_string = file.read()
input_list = input_string.split("\n")

lights = []
for curr_light in input_list:
    temp_light = curr_light.split(",")
    tl_x = int(temp_light[0])
    tl_y = int(temp_light[1])
    tl_z = int(temp_light[2])

    lights.append((tl_x, tl_y, tl_z))

distance = []
for row in range(len(lights)):
    for col in range(len(lights)):
        if row > col:
            light1 = lights[row]
            light2 = lights[col]
            curr_dist = ((light1[0]-light2[0])**2 + (light1[1]-light2[1])**2 + (light1[2]-light2[2])**2)**0.5
            distance.append((curr_dist, (row, col)))
distance.sort()

circuits = []
for i in range(len(lights)):
    circuits.append([i])

for i in range(1000):
    (curr_dist, (light1, light2)) = distance[i]

    circuit1 = []
    circuit2 = []
    for curr_circuit in circuits:
        if light1 in curr_circuit:
            circuit1 = curr_circuit
        if light2 in curr_circuit:
            circuit2 = curr_circuit

    if circuit1 in circuits:
        circuits.remove(circuit1)
    if circuit2 in circuits:
        circuits.remove(circuit2)

    new_circuit = []
    for light in circuit1:
        if light not in new_circuit:
            new_circuit.append(light)
    
    for light in circuit2:
        if light not in new_circuit:
            new_circuit.append(light)

    circuits.append(new_circuit)

circuits.sort(key=len, reverse=True)

total_p1 = len(circuits[0]) * len(circuits[1]) * len(circuits[2])
print(total_p1)

i = 1001
while(len(circuits) >= 2):
    (curr_dist, (light1, light2)) = distance[i]

    circuit1 = []
    circuit2 = []
    for curr_circuit in circuits:
        if light1 in curr_circuit:
            circuit1 = curr_circuit
        if light2 in curr_circuit:
            circuit2 = curr_circuit

    if circuit1 in circuits:
        circuits.remove(circuit1)
    if circuit2 in circuits:
        circuits.remove(circuit2)

    new_circuit = []
    for light in circuit1:
        if light not in new_circuit:
            new_circuit.append(light)
    
    for light in circuit2:
        if light not in new_circuit:
            new_circuit.append(light)

    circuits.append(new_circuit)
    i += 1

(ll1_x, ll1_y, ll1_z) = lights[light1]
(ll2_x, ll2_y, ll2_z) = lights[light2]

total_p2 = ll1_x * ll2_x

print(total_p2)