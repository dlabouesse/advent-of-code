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
            return ''
        elif (is_opening_chunk_char(char)):
            expected_char_for_closing.append(get_closing_chunk_char(char))
        else:
            del expected_char_for_closing[-1]
    return expected_char_for_closing

def get_autocomplete_score(closing_chars):
    score = 0
    closing_chars.reverse()
    for char in closing_chars:
        score *= 5
        if (char) == '>':
            score += 4
        elif (char) == ')':
            score += 1
        elif (char) == ']':
            score += 2
        elif (char) == '}':
            score += 3
    return score

def autocomplete_chunks(chunks_list):
    autocomplete_scores = []
    for chunks in chunks_list:
        closing_chars = parse_chunks(chunks)
        if(closing_chars):
            autocomplete_scores.append(get_autocomplete_score(closing_chars))
    # print(autocomplete_scores)
    autocomplete_scores.sort()
    print(autocomplete_scores[int((len(autocomplete_scores)-1)/2)])

def main():
    chunks_list = read_input()

    autocomplete_chunks(chunks_list)

if __name__ == "__main__":
    main()
