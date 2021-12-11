def read_input():
    map = []
    with open("input.txt", "r") as f:
        for row in f:
            current_row = []
            for octopus in row.rstrip("\n"):
                current_row.append  (int(octopus))
            map.append(current_row)
    return map

def print_map(map):
    for raw in map:
        for col in raw:
            print(col,end='')
        print("")
    print("")

def octopus_flash(map, position):
    if (position[0] > 0):
        if (position[1] > 0):
            map[position[1]-1][position[0]-1] += 1
        if (position[1] < len(map) - 1):
            map[position[1]+1][position[0]-1] += 1
        map[position[1]][position[0]-1] += 1
    if (position[0] < len(map[0]) -1 ):
        if (position[1] > 0):
            map[position[1]-1][position[0]+1] += 1
        if (position[1] < len(map) - 1):
            map[position[1]+1][position[0]+1] += 1
        map[position[1]][position[0]+1] += 1
    if (position[1] > 0):
        map[position[1]-1][position[0]] += 1
    if (position[1] < len(map) -1 ):
        map[position[1]+1][position[0]] += 1
    pass

def new_step(map):
    for y in range(len(map)):
        for x in range(len(map[y])):
            map[y][x] += 1

    flashes_occured = True
    already_flashed = []
    while (flashes_occured):
        flashes_occured =  False
        for y in range(len(map)):
            for x in range(len(map[y])):
                if (map[y][x] > 9 and (x,y) not in already_flashed):
                    # print('Octopus flash at ({}, {})'.format(x, y))
                    octopus_flash(map, (x, y))
                    flashes_occured = True
                    already_flashed.append((x, y))

    nb_flashes = 0
    for y in range(len(map)):
        for x in range(len(map[y])):
            if (map[y][x] > 9):
                nb_flashes += 1
                map[y][x] = 0
    return nb_flashes

def main():
    map = read_input()

    nb_flashes = 0
    for i in range (100):
        nb_flashes += new_step(map)
        # print_map(map)

    print(nb_flashes)

if __name__ == "__main__":
    main()
