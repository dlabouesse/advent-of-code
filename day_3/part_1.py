def get_rates(counters):
    gamma_rate = ""
    epsilon_rate = ""
    for i in range(len(counters)):
        if (counters[i]['0'] > counters[i]['1']):
            gamma_rate+="0"
            epsilon_rate+="1"
        elif (counters[i]['0'] < counters[i]['1']):
            gamma_rate+="1"
            epsilon_rate+="0"
        else:
            print("Counters are equal!")
    return (gamma_rate, epsilon_rate)

def main():
    bits = []
    with open("input.txt", "r") as f:
        for line in f:
            bits.append(line.rstrip("\n"))

    counters = [{'0': 0, '1': 0} for x in range(len(bits[0]))]
    for i in range(len(bits)):
        for j in range(len(bits[i])):
            if (bits[i][j] == "0"):
                counters[j]['0'] += 1
            elif (bits[i][j] == "1"):
                counters[j]['1'] += 1
            else:
                print("Something weird happened!")

    (gamma_rate, epsilon_rate) = get_rates(counters)
    print(int(gamma_rate, 2) * int(epsilon_rate, 2))

if __name__ == "__main__":
    main()
