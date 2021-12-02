f = open("input.txt", "r")
position = [0, 0]
for line in f:
    if (line.split(' ')[0] == 'forward'):
        position[0] += int(line.split(' ')[1])
    elif (line.split(' ')[0] == 'down'):
        position[1] += int(line.split(' ')[1])
    elif (line.split(' ')[0] == 'up'):
        position[1] -= int(line.split(' ')[1])

print(position[0]*position[1])
