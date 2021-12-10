def read_input():
    chunks_list = []
    with open("input.txt", "r") as f:
        for row in f:
            chunks_list.append(row.rstrip("\n"))
    return chunks_list

def get_closing_chunk_char(opening_char):
    if (opening_char) == '<':
        return '>'
    elif (opening_char) == '(':
        return ')'
    elif (opening_char) == '[':
        return ']'
    elif (opening_char) == '{':
        return '}'
    else:
        return 'coucou'

def is_opening_chunk_char(char):
    if (char == '<' or char == '(' or char =='{' or char == '['):
        return True
    return False

def parse_chunks(chunks):
    expected_char_for_closing = []
    for char in list(chunks):
        if (not is_opening_chunk_char(char) and char != expected_char_for_closing[-1]):
            # print('Corrupted chunk: found {} but expected {}'.format(char, expected_char_for_closing[-1]))
            return char
        elif (is_opening_chunk_char(char)):
            expected_char_for_closing.append(get_closing_chunk_char(char))
        else:
            del expected_char_for_closing[-1]
    return ''

def get_illegal_chars(chunks_list):
    illegal_chars = {
        '>': 0,
        ')': 0,
        ']': 0,
        '}': 0
    }
    for chunks in chunks_list:
        illegal_char = parse_chunks(chunks)
        if(illegal_char):
            illegal_chars[illegal_char] += 1
    return illegal_chars

def get_score(illegal_chars):
    score = 0
    for illegal_char, value in illegal_chars.items():
        if (illegal_char) == '>':
            score += int(25137*value)
        elif (illegal_char) == ')':
            score += int(3*value)
        elif (illegal_char) == ']':
            score += int(57*value)
        elif (illegal_char) == '}':
            score += int(1197*value)
    return score

def main():
    chunks_list = read_input()

    illegal_chars = get_illegal_chars(chunks_list)

    # print(illegal_chars)

    print(get_score(illegal_chars))

if __name__ == "__main__":
    main()
