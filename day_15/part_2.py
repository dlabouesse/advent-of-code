import tools.readfile as readfile
from copy import deepcopy

# Look for backward paths that could have a lower total risk, and explore them recusively
def readjust_value(reduced_risk_level_map, risk_level_map, position, line_limit):
    # Ignore if the position correponds to the start position, or if they are outside the map
    if(position[0] < 0 or position[0] > len(reduced_risk_level_map[0]) - 1 or position[1] < line_limit or position[1] > len(reduced_risk_level_map) - 1 or (position[0] == 0 and position[1] == 0)):
        return
    readjusted = False
    # Left readjustment
    if(position[0] > 0 and not(position[0] == 1 and position[1] == 0)):
        if(reduced_risk_level_map[position[1]][position[0]] > reduced_risk_level_map[position[1]][position[0] - 1] + risk_level_map[position[1]][position[0]]):
            reduced_risk_level_map[position[1]][position[0]] = reduced_risk_level_map[position[1]][position[0] - 1] + risk_level_map[position[1]][position[0]]
            readjusted = True
    # Right readjustment
    if(position[0] < len(reduced_risk_level_map[position[1]]) - 1):
        if(reduced_risk_level_map[position[1]][position[0]] > reduced_risk_level_map[position[1]][position[0] + 1] + risk_level_map[position[1]][position[0]]):
            reduced_risk_level_map[position[1]][position[0]] = reduced_risk_level_map[position[1]][position[0] + 1] + risk_level_map[position[1]][position[0]]
            readjusted = True
    # Up readjustment
    if(position[1] > line_limit and not(position[0] == 0 and position[1] == 1)):
        if(reduced_risk_level_map[position[1]][position[0]] > reduced_risk_level_map[position[1] - 1][position[0]] + risk_level_map[position[1]][position[0]]):
            reduced_risk_level_map[position[1]][position[0]] = reduced_risk_level_map[position[1] - 1][position[0]] + risk_level_map[position[1]][position[0]]
            readjusted = True
    # Down readjustment
    if(position[1] < len(reduced_risk_level_map) - 1):
        if(reduced_risk_level_map[position[1]][position[0]] > reduced_risk_level_map[position[1] + 1][position[0]] + risk_level_map[position[1]][position[0]]):
            reduced_risk_level_map[position[1]][position[0]] = reduced_risk_level_map[position[1] + 1][position[0]] + risk_level_map[position[1]][position[0]]
            readjusted = True
    if(readjusted):
        readjust_value(reduced_risk_level_map, risk_level_map, (position[0]+1, position[1]), line_limit)
        readjust_value(reduced_risk_level_map, risk_level_map, (position[0]-1, position[1]), line_limit)
        readjust_value(reduced_risk_level_map, risk_level_map, (position[0], position[1]+1), line_limit)
        readjust_value(reduced_risk_level_map, risk_level_map, (position[0], position[1]-1), line_limit)

def prepare_for_reduce(weighted_map):
    for i in reversed(range(0, len(weighted_map[-1]))):
        if (i > 0):
            weighted_map[-1][i-1] += weighted_map[-1][i]

# For each line, from the bottom to the top, recalculates equivalent lowest total risk for each point in order to interatively reduce the map size
def reduce_map(reduced_risk_level_map, risk_level_map, line_index):
    for i in reversed(range(0, len(reduced_risk_level_map[line_index]))):
        # Add the risk value of the current point with the lowest total risk of the adjacent position closer to the destination (either the right or down value)
        if (i == len(reduced_risk_level_map[line_index]) - 1):
            reduced_risk_level_map[line_index-1][i] += reduced_risk_level_map[line_index][i]
        else:
            reduced_risk_level_map[line_index-1][i] += min(reduced_risk_level_map[line_index][i], reduced_risk_level_map[line_index-1][i+1])

    # Now that all the values for the current line have been updated, it's time to verify the presence of potential backwards paths
    for i in range(0, len(reduced_risk_level_map[line_index-1])):
        readjust_value(reduced_risk_level_map, risk_level_map, (i, line_index), line_index-1)

def get_lowest_total_risk(reduced_risk_level_map):
    return min(reduced_risk_level_map[1][0], reduced_risk_level_map[0][1])

def make_it_bigger(risk_level_map):
    bigger_risk_level_map = []
    for y in range(len(risk_level_map)):
        new_line = []
        for i in range(5):
            for x in range(len(risk_level_map[y])):
                if i == 0:
                    new_line.append(risk_level_map[y][x])
                else:
                    if(new_line[x+(i-1)*len(risk_level_map[0])] < 9):
                        new_line.append(new_line[x+(i-1)*len(risk_level_map[0])] + 1)
                    else:
                        new_line.append(1)
        bigger_risk_level_map.append(new_line)

    for i in range(1, 5):
        for y in range(len(risk_level_map)):
            new_line = []
            for x in range(len(bigger_risk_level_map[y])):
                if (bigger_risk_level_map[y+(i-1)*len(risk_level_map)][x] < 9):
                    new_line.append(bigger_risk_level_map[y+(i-1)*len(risk_level_map)][x] + 1)
                else:
                    new_line.append(1)
            bigger_risk_level_map.append(new_line)

    return bigger_risk_level_map

def main():
    lines = readfile.read_lines("input.txt")
    risk_level_map = [list(map(int, line)) for line in lines]

    risk_level_map = make_it_bigger(risk_level_map)

    reduced_risk_level_map = deepcopy(risk_level_map)

    prepare_for_reduce(reduced_risk_level_map)

    for line_index in reversed(range(1, len(risk_level_map))):
        reduce_map(reduced_risk_level_map, risk_level_map, line_index)

    print(get_lowest_total_risk(reduced_risk_level_map))


if __name__ == "__main__":
    main()
