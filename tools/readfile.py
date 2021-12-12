def read_map(input):
    map = []
    with open(input, "r") as f:
        for row in f:
            current_row = []
            for char in row.rstrip("\n"):
                current_row.append(char)
            map.append(current_row)
    return map

def print_map(map):
    for raw in map:
        for col in raw:
            print(col,end='')
        print("")
    print("")

def read_lines(input):
    lines = []
    with open(input, "r") as f:
        for row in f:
            lines.append(row.rstrip("\n"))
    return lines
