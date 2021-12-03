def get_counters(bits):
    counters = [{'0': 0, '1': 0} for x in range(len(bits[0]))]
    for i in range(len(bits)):
        for j in range(len(bits[i])):
            if (bits[i][j] == "0"):
                counters[j]['0'] += 1
            elif (bits[i][j] == "1"):
                counters[j]['1'] += 1
            else:
                print("Something weird happened!")
    return counters

def filter_bits(bits, bit_index, bit_value):
    return list(filter(lambda bit: bit[bit_index] == bit_value, bits))

def find_oxygen_generator_rating(bits):
    for i in range(len(bits[0])):
        counters = get_counters(bits)
        if counters[i]['0'] > counters[i]['1']:
            bits = filter_bits(bits, i, '0')
        elif counters[i]['0'] > counters[i]['1']:
            bits = filter_bits(bits, i, '1')
        else:
            bits = filter_bits(bits, i, '1')
        if(len(bits) == 1):
            return(bits[0])

def find_CO2_scrubber_rating(bits):
    for i in range(len(bits[0])):
        counters = get_counters(bits)
        if counters[i]['0'] > counters[i]['1']:
            bits = filter_bits(bits, i, '1')
        elif counters[i]['0'] > counters[i]['1']:
            bits = filter_bits(bits, i, '0')
        else:
            bits = filter_bits(bits, i, '0')
        if(len(bits) == 1):
            return(bits[0])

def main():
    bits = []
    with open("input.txt", "r") as f:
        for line in f:
            bits.append(line.rstrip("\n"))

    oxygen_generator_rating = find_oxygen_generator_rating(bits)
    CO2_scrubber_rating = find_CO2_scrubber_rating(bits)

    print('oxygen_generator_rating:\t{}'.format(oxygen_generator_rating))
    print('oxygen_generator_rating:\t{}'.format(int(oxygen_generator_rating,2)))
    print('CO2_scrubber_rating:\t\t{}'.format(CO2_scrubber_rating))
    print('CO2_scrubber_rating:\t\t{}'.format(int(CO2_scrubber_rating, 2)))
    print('Output:\t\t\t\t{}'.format(int(oxygen_generator_rating,2) * int(CO2_scrubber_rating, 2)))

if __name__ == "__main__":
    main()
