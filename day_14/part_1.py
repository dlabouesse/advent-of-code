import tools.readfile as readfile

def parse_input(lines):
    input = {
        'formula': '',
        'transformations': {}
    }
    first_line = True

    for line in lines:
        if (first_line):
            input['formula'] = line
            first_line = False
        elif (line != ''):
            input['transformations'][line.split(' -> ')[0]] = line.split(' -> ')[1]
    return input

def apply_transformations(input):
    new_string = input['formula']
    for i in range(len(input['formula'])-1):
        value = input['formula'][i]+input['formula'][i+1]
        new_string = new_string[:i*2+1] + input['transformations'][value] + new_string[i*2+1:]
    input['formula'] = new_string

def get_score(formula):
    sums = {}
    for char in formula:
        if char in sums:
            sums[char] += 1
        else:
            sums[char] = 1
    # print(sums)
    max_val = max(sums.values())
    min_val = min(sums.values())

    return max_val - min_val

def main():
    lines = readfile.read_lines("input.txt")

    input = parse_input(lines)

    for i in range(10):
        apply_transformations(input)

    print(get_score(input['formula']))

if __name__ == "__main__":
    main()
