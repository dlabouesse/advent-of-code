import tools.readfile as readfile

def find_routes(caves_map, position, path, routes, small_cave):
    for destination in caves_map[position]:
        if (path.count(small_cave) < 2):
                small_cave = ''
        # print("{} -> ({}) <= {}".format(path, caves_map[position], destination))
        if destination == 'end':
            path.append(destination)
            routes.append(path.copy())
            # print("\tNew route found {}".format(path))
            continue
        elif (destination.upper() == destination or destination not in path or not small_cave):
            if (destination in path and destination.lower() == destination):
                small_cave = destination
            current_path = '-'.join(path)
            path.append(destination)
            find_routes(caves_map, destination, path, routes, small_cave)
            # print("Resuming from {} (small_cave: {})".format(current_path, small_cave))
            path = current_path.split('-')
            continue
        # print("{} -> {} (small_cave: {}): invalid path".format(path, destination, small_cave))

def parse_map(input):
    caves_map = {}
    for line in input:
        cave_1 = line.split('-')[0]
        cave_2 = line.split('-')[1]
        if (cave_1 in caves_map and cave_2 != 'start' and cave_1 != 'end'):
            caves_map[cave_1].append(cave_2)
        elif (cave_2 != 'start' and cave_1 != 'end'):
            caves_map[cave_1] = [cave_2]
        if (cave_2 in caves_map and cave_1 != 'start' and cave_2 != 'end'):
            caves_map[cave_2].append(cave_1)
        elif (cave_1 != 'start' and cave_2 != 'end'):
            caves_map[cave_2] = [cave_1]
    return caves_map

def main():
    lines = readfile.read_lines("input.txt")
    caves_map = parse_map(lines)

    routes = []
    find_routes(caves_map, 'start', ['start'], routes, '')
    print(len(routes))

if __name__ == "__main__":
    main()
