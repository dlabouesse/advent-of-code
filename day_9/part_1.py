def print_map(map):
    for raw in map:
        for col in raw:
            print(col,end='')
        print("")
    print("")

def read_input():
    map = []
    with open("input.txt", "r") as f:
        for row in f:
            current_row = []
            for col in row.rstrip("\n"):
                current_row.append(int(col))
            map.append(current_row)
    return map

def get_value_at_position(positions, map):
    return map[positions[1]][positions[0]]

def detect_lowest_point(positions, map):
    if (positions[0] > 0):
        if (map[positions[1]][positions[0]-1] <= get_value_at_position(positions, map)):
            return False
    if (positions[0] < len(map[0])-1):
        if (map[positions[1]][positions[0]+1] <= get_value_at_position(positions, map)):
            return False
    if (positions[1] > 0):
        if (map[positions[1]-1][positions[0]] <= get_value_at_position(positions, map)):
            return False
    if (positions[1] < len(map)-1):
        if (map[positions[1]+1][positions[0]] <= get_value_at_position(positions, map)):
            return False
    return True

def calculate_risk_level(lowest_points):
    risk_level = 0
    for lowest_point in lowest_points:
        risk_level += lowest_point['value']+1
    return risk_level

def main():
    map = read_input()
    # print_map(map)

    lowest_points = []

    for i in range(len(map)):
        for j in range(len(map[i])):
            if(detect_lowest_point((j, i), map)):
                lowest_points.append({'value': get_value_at_position((j, i), map), 'x': j, 'y': i})

    print(calculate_risk_level(lowest_points))


if __name__ == "__main__":
    main()
