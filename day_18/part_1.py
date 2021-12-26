import tools.readfile as readfile
import re
import math

def get_left_number(string):
    match_pos = None
    number = []
    i = len(string)-1
    while i >= 0:
        if (string[i].isnumeric()):
            while (string[i].isnumeric()):
                number.insert(0, string[i])
                i -=  1
            match_pos = i + 1
            break
        i -= 1
    return (match_pos, "".join(number))

def get_right_number(string):
    match_pos = None
    number = []
    i = 0
    while i < len(string):
        if (string[i].isnumeric()):
            match_pos = i
            while (string[i].isnumeric()):
                number.append(string[i])
                i +=  1
            break
        i += 1
    return (match_pos, "".join(number))

def explode_pair(pair):
    nested_indice = 0
    pair_to_explode = []
    i =  0
    while i < len(pair):
        if pair[i] == '[':
            nested_indice += 1
        elif pair[i] == ']':
            nested_indice -= 1
        if nested_indice == 5 and pair[i].isnumeric():
            pos = i
            val = ''
            while pair[i].isnumeric():
                val += pair[i]
                i += 1
            pair_to_explode.append({
                    'pos': pos,
                    'val': val
                })
        i += 1

    if (not len(pair_to_explode)):
        return False

    left_number_pos, left_number_val = get_left_number("".join(pair[:pair_to_explode[0]['pos']-1]))

    if(left_number_pos):
        new_val = str(int(left_number_val) + int(pair_to_explode[0]['val']))
        for i in range(len(left_number_val)):
            del pair[left_number_pos]
        for i in range(len(new_val)-1, -1, -1):
            pair.insert(left_number_pos, new_val[i])

        pair_to_explode[0]['pos'] += len(new_val) - len(left_number_val)
        pair_to_explode[1]['pos'] += len(new_val) - len(left_number_val)

    right_number_pos, right_number_val = get_right_number("".join(pair[pair_to_explode[1]['pos']+len(pair_to_explode[1]['val']):]))

    if(right_number_pos):
        right_number_pos += pair_to_explode[1]['pos']+len(pair_to_explode[1]['val'])
        new_val = str(int(right_number_val) + int(pair_to_explode[1]['val']))
        for i in range(len(right_number_val)):
            del pair[right_number_pos]
        for i in range(len(new_val)-1, -1, -1):
            pair.insert(right_number_pos, new_val[i])

    del pair[pair_to_explode[0]['pos']-1:pair_to_explode[1]['pos']+len(pair_to_explode[1]['val'])+1]
    pair.insert(pair_to_explode[0]['pos']-1,'0')

    return True

def split_pair(pair):
    x = re.search(r"(\d{2,})", "".join(pair))
    if (not x):
        return False
    del pair[x.span()[0]:x.span()[1]]
    pair.insert(x.span()[0],']')
    for char in str(math.ceil(int(x.group())/2))[::-1]:
        pair.insert(x.span()[0],char)
    pair.insert(x.span()[0],',')
    for char in str(math.floor(int(x.group())/2))[::-1]:
        pair.insert(x.span()[0],char)
    pair.insert(x.span()[0],'[')
    return True

def reduce_pair(pair):
    while(True):
        if (explode_pair(pair)):
            continue
        if (split_pair(pair)):
            continue
        return

def add_pair(pair_1, pair_2):
    pair = '[' + str("".join(pair_1)) + ',' + str("".join(pair_2)) + ']'
    return list(pair)

def get_magnitude(pair):
    nested_level = 0
    split_index = None
    for i in range(len(pair)):
        if pair[i] == '[':
            nested_level += 1
        elif pair[i] == ']':
            nested_level -= 1
        if pair[i] == ',' and nested_level ==  1:
            split_index = i
    left_part = pair[1:split_index]
    right_part = pair[split_index+1:-1]
    if ("".join(left_part).isnumeric() and "".join(right_part).isnumeric()):
        return 3 * int("".join(left_part)) + 2 * int("".join(right_part))
    elif("".join(left_part).isnumeric()):
        return 3 * int("".join(left_part)) + 2 * get_magnitude(right_part)
    elif("".join(right_part).isnumeric()):
        return 3 * get_magnitude(left_part) + 2 * int("".join(right_part))
    else:
        return 3 * get_magnitude(left_part) + 2 * get_magnitude(right_part)

def main():
    lines = readfile.read_lines("input.txt")
    pair = list(lines[0])

    for line in lines[1:]:
        pair = add_pair(pair, list(line))
        reduce_pair(pair)
    print("".join(pair))

    print(get_magnitude(pair))

if __name__ == "__main__":
    main()
