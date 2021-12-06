def calculate_map_size(lines_coordinates):
    max_x = 0
    max_y = 0
    for line_coordinates in lines_coordinates:
        max_x = max(line_coordinates['start']['x'], line_coordinates['end']['x'], max_x)
        max_y = max(line_coordinates['start']['y'], line_coordinates['end']['y'], max_y)
    return max_x+1, max_y+1

def read_coordinates():
    lines_coordinates = []
    with open("input.txt", "r") as f:
        for line in f:
            lines_coordinates.append({
                "start": {
                    "x": int(line.rstrip("\n").replace(" ", "").split('->')[0].split(',')[0]),
                    "y": int(line.rstrip("\n").replace(" ", "").split('->')[0].split(',')[1]),
                },
                "end": {
                    "x": int(line.rstrip("\n").replace(" ", "").split('->')[1].split(',')[0]),
                    "y": int(line.rstrip("\n").replace(" ", "").split('->')[1].split(',')[1]),
                }
            })

    return lines_coordinates

def initialize_empty_map(max):
    map = []
    for raw in range(max[1]):
        map.append(['.' for x in range(max[0])])
    return map

def print_map(map):
    for raw in map:
        for col in raw:
            print(col,end='')
        print("")
    print("")

def increase_map(map, coordinates):
    # print("increase_map")
    # print(coordinates)
    x = coordinates[0]
    y = coordinates[1]
    if (map[y][x] == '.'):
        map[y][x] = 1
    else:
        map[y][x] += 1

def update_map(map, line_coordinates):
    # print("update map")
    # print(line_coordinates)
    if (line_coordinates['start']['x'] == line_coordinates['end']['x']):
        min_y = min(line_coordinates['start']['y'], line_coordinates['end']['y'])
        max_y = max(line_coordinates['start']['y'], line_coordinates['end']['y'])
        for i in range(min_y, max_y+1):
            increase_map(map, (line_coordinates['start']['x'], i))
    elif (line_coordinates['start']['y'] == line_coordinates['end']['y']):
        min_x = min(line_coordinates['start']['x'], line_coordinates['end']['x'])
        max_x = max(line_coordinates['start']['x'], line_coordinates['end']['x'])
        for i in range(min_x, max_x+1):
            increase_map(map, (i, line_coordinates['start']['y']))
    else:
        min_x = min(line_coordinates['start']['x'], line_coordinates['end']['x'])
        min_y = min(line_coordinates['start']['y'], line_coordinates['end']['y'])
        max_x = max(line_coordinates['start']['x'], line_coordinates['end']['x'])
        max_y = max(line_coordinates['start']['y'], line_coordinates['end']['y'])
        y_offset = 0
        if (min_x == line_coordinates['start']['x'] and min_y == line_coordinates['start']['y'] or
            min_x == line_coordinates['end']['x'] and min_y == line_coordinates['end']['y']):
            # print(line_coordinates)
            for i in range(min_x,max_x+1):
                increase_map(map, (i, min_y+y_offset))
                y_offset += 1
        else:
            # print(line_coordinates)
            for i in range(min_x,max_x+1):
                increase_map(map, (i, max_y-y_offset))
                y_offset += 1

def calculate_nb_of_danger_zone(map, danger_threshold):
    nb_of_danger_zone = 0
    for raw in map:
        for value in raw:
            if (value != '.' and value >= danger_threshold):
                nb_of_danger_zone += 1
    return nb_of_danger_zone


def main():
    lines_coordinates = read_coordinates()
    # print(lines_coordinates)

    map = initialize_empty_map(calculate_map_size(lines_coordinates))

    for line_coordinates in lines_coordinates:
        update_map(map, line_coordinates)

    # print_map(map)

    print(calculate_nb_of_danger_zone(map, 2))

if __name__ == "__main__":
    main()
