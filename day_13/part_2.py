import tools.readfile as readfile

def read_instruction(lines):
    instructions = {
        'dots': [],
        'folds': []
    }
    are_dots = True
    for line in lines:
        if line == '':
            are_dots = False
            continue
        if(are_dots):
            instructions['dots'].append({
                'x': int(line.split(',')[0]),
                'y': int(line.split(',')[1])
            })
        else:
            instructions['folds'].append({
                'axis': line.split(' ')[2].split('=')[0],
                'coordinate': int(line.split(' ')[2].split('=')[1])
            })
    return instructions

def get_map_size(instructions):
    max_x = 0
    max_y = 0
    for dot in instructions['dots']:
        max_x = max(max_x, dot['x'])
        max_y = max(max_y, dot['y'])
    return (max_x, max_y)

def get_folded_size(instructions):
    min_x = get_map_size(instructions)[0]+1
    min_y = get_map_size(instructions)[1]+1
    for fold in instructions['folds']:
        if (fold['axis'] == 'x'):
            min_x = min(min_x, fold['coordinate'])
        elif (fold['axis'] == 'y'):
            min_y = min(min_y, fold['coordinate'])
    return (min_x, min_y)

def create_map(instructions):
    (map_x, map_y) = get_map_size(instructions)
    map = []
    for y in range(map_y+1):
        map.append(['.' for x in range(map_x+1)])
    return map

def add_dots(map, dots):
    for dot in dots:
        map[dot['y']][dot['x']] = '#'

def proceed_folds(map, folds):
    for fold in folds:
        if (fold['axis'] == 'x'):
            for y in range(len(map)):
                for x in range(len(map[y])):
                    if (x > fold['coordinate'] and map[y][x] == '#'):
                        map[y][fold['coordinate']-(x-fold['coordinate'])] = '#'
        elif (fold['axis'] == 'y'):
            for y in range(len(map)):
                for x in range(len(map[y])):
                    if (y > fold['coordinate'] and map[y][x] == '#'):
                        map[fold['coordinate']-(y-fold['coordinate'])][x] = '#'

def print_map_with_limits(map, size):
    for y in range(size[1]):
        for x in range(size[0]):
            print(map[y][x],end='')
        print("")
    print("")

def main():
    lines = readfile.read_lines("input.txt")
    instructions = read_instruction(lines)
    map = create_map(instructions)

    add_dots(map, instructions['dots'])

    proceed_folds(map, instructions['folds'])
    print_map_with_limits(map, get_folded_size(instructions))

if __name__ == "__main__":
    main()
