def sort_string(string):
    return "".join(sorted(string))

def read_input():
    four_digits_list = []
    with open("input.txt", "r") as f:
        for line in f:
            signal_pattern_entries = {}
            for signal_pattern_entry in line.rstrip("\n").split('|')[0].strip().split(' '):
                signal_pattern_entries[signal_pattern_entry] = ''

            output_digits = []
            for output_digit in line.rstrip("\n").split('|')[1].strip().split(' '):
                output_digits.append({output_digit : ''})

            four_digits_list.append({'signal_pattern_entries': signal_pattern_entries, 'output_digits': output_digits})
    return four_digits_list

def decode_entries(four_digits_list):
    for i in range(len(four_digits_list)):
        for signal_pattern_entry in four_digits_list[i]['signal_pattern_entries'].keys():
            if (len(signal_pattern_entry) == 2):
                four_digits_list[i]['signal_pattern_entries'][signal_pattern_entry] = 1
            elif (len(signal_pattern_entry) == 4):
                four_digits_list[i]['signal_pattern_entries'][signal_pattern_entry] = 4
            elif (len(signal_pattern_entry) == 3):
                four_digits_list[i]['signal_pattern_entries'][signal_pattern_entry] = 7
            elif (len(signal_pattern_entry) == 7):
                four_digits_list[i]['signal_pattern_entries'][signal_pattern_entry] = 8

def decode_outputs(four_digits_list):
    for i in range(len(four_digits_list)):
        for signal_pattern_entry, value in four_digits_list[i]['signal_pattern_entries'].items():
            if (value):
                for j in range(4):
                    output_digit = list(four_digits_list[i]['output_digits'][j].keys())[0]
                    if (sort_string(signal_pattern_entry) == sort_string(output_digit)):
                        four_digits_list[i]['output_digits'][j][output_digit] = value

def count_decoded_outputs(four_digits_list):
    sum = 0
    for four_digits in four_digits_list:
        for output_digit in four_digits['output_digits']:
            if(list(output_digit.values())[0]):
                sum += 1
    return sum

def main():
    four_digits_list = read_input()

    decode_entries(four_digits_list)

    decode_outputs(four_digits_list)

    print(count_decoded_outputs(four_digits_list))

if __name__ == "__main__":
    main()
