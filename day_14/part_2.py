import tools.readfile as readfile

def parse_input(lines):
    input = {
        'transformations': {},
        'formula_pairs' : {},
        'sums': {}
    }
    first_line = True

    for line in lines:
        if (first_line):
            for i in range(len(line)-1):
                value = line[i]+line[i+1]
                if value in input['formula_pairs']:
                    input['formula_pairs'][value] += 1
                else:
                    input['formula_pairs'][value] = 1
            for char in line:
                if char in input['sums']:
                    input['sums'][char] += 1
                else:
                    input['sums'][char] = 1
            first_line = False
        elif (line != ''):
            input['transformations'][line.split(' -> ')[0]] = line.split(' -> ')[1]
    return input

def apply_transformations_using_pairs(input):
    new_pairs = {}
    for pair in input['formula_pairs']:
        new_pair1 = pair[0]+input['transformations'][pair]
        new_pair2 = input['transformations'][pair]+pair[1]
        if new_pair1 in new_pairs:
            new_pairs[new_pair1] += input['formula_pairs'][pair]
        else:
            new_pairs[new_pair1] = input['formula_pairs'][pair]
        if new_pair2 in new_pairs:
            new_pairs[new_pair2] += input['formula_pairs'][pair]
        else:
            new_pairs[new_pair2] = input['formula_pairs'][pair]
        if input['transformations'][pair] in input['sums']:
            input['sums'][input['transformations'][pair]] += input['formula_pairs'][pair]
        else:
            input['sums'][input['transformations'][pair]] = input['formula_pairs'][pair]
    input['formula_pairs'] = new_pairs.copy()

def get_score_using_pairs(sums):
    max_val = max(sums.values())
    min_val = min(sums.values())

    return max_val - min_val

def main():
    lines = readfile.read_lines("input.txt")

    input = parse_input(lines)

    for i in range(40):
        apply_transformations_using_pairs(input)

    print(get_score_using_pairs(input['sums']))

if __name__ == "__main__":
    main()
