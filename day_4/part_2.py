import re
from collections import OrderedDict

def print_grid(grid):
    for raw in grid:
        print("{}\t{}\t{}\t{}\t{}".format(raw[0], raw[1], raw[2], raw[3], raw[4]))
    print("")

def proceed_draw(grids, grids_results, drawn_number):
    matching_grids = []
    for grid_index in range(len(grids)):
        for raw_index in range(len(grids[grid_index])):
            for col_index in range(len(grids[grid_index][raw_index])):
                if grids[grid_index][raw_index][col_index] == drawn_number:
                    # print("Number {} found in grid #{}".format(drawn_number, grid_index))
                    grids_results[grid_index][raw_index][col_index] = 1
                    matching_grids.append(grid_index)

    return matching_grids

def check_for_winning_grids(grids_results, grid_indexes):
    winning_grids = []
    for grid_index in grid_indexes:
        col_candidates = list(range(5))
        for raw in grids_results[grid_index]:
            raw_candidate = True
            zero_indexes = [i for i, x in enumerate(raw) if x == 0]
            for zero_index in zero_indexes:
                raw_candidate = False
                if zero_index in col_candidates:
                    col_candidates.remove(zero_index)
            if raw_candidate:
                winning_grids.append(grid_index)
        if len(col_candidates):
            winning_grids.append(grid_index)
    return winning_grids

def calculate_winning_score(grid, grid_result, drawn_number):
    sum = 0
    for raw_index in range(len(grid_result)):
        for col_index in range(len(grid_result[raw_index])):
            if grid_result[raw_index][col_index] == 0:
                sum+=int(grid[raw_index][col_index])
    # print('sum: ', sum)
    # print('drawn_number: ', drawn_number)
    return sum * drawn_number


def main():
    draw = []
    grids = []
    grids_results = []
    with open("input.txt", "r") as f:
        first_line = True
        current_grid = []
        current_grid_result = []
        for line in f:
            if first_line:
                for number in line.rstrip("\n").split(','):
                    draw.append(number)
            else:
                if line.rstrip("\n") == "":
                    current_grid = []
                    current_grid_result = []
                else:
                    extracted_number = (re.search('^\s*(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s+(\d+)\s*$', line.rstrip("\n"), re.IGNORECASE))
                    raw = [extracted_number.group(1), extracted_number.group(2), extracted_number.group(3), extracted_number.group(4), extracted_number.group(5)]
                    current_grid.append(raw)
                    current_grid_result.append([0 for x in raw])
                    if len(current_grid) == 5:
                        grids.append(current_grid)
                        grids_results.append(current_grid_result)
            first_line = False

    # print('draw', draw)
    # print('grids', grids)
    # print('len(grids)', len(grids))
    # print('grids_results', grids_results)

    last_winning_score = 0
    for drawn_number in draw:
        matching_grids = []
        matching_grids = proceed_draw(grids, grids_results, drawn_number)
        winning_grids = check_for_winning_grids(grids_results, matching_grids)
        if len(winning_grids):
            last_winning_score = calculate_winning_score(grids[winning_grids[-1]], grids_results[winning_grids[-1]], int(drawn_number))
            for winning_grid in list(reversed(OrderedDict.fromkeys(winning_grids))):
                del grids[winning_grid]
                del grids_results[winning_grid]

    print(last_winning_score)
    return 0


if __name__ == "__main__":
    main()
