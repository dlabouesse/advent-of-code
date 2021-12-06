def update_lanternfishes(lanternfishes):
    new_lanternfishes = lanternfishes[0]
    del lanternfishes[0]
    lanternfishes[6] += new_lanternfishes
    lanternfishes.append(new_lanternfishes)

def read_inital_state():
    lanternfishes = [0 for x in range(9)]
    with open("input.txt", "r") as f:
        for line in f:
            for value in line.split(','):
                lanternfishes[int(value)] += 1
    return lanternfishes

def main():
    lanternfishes = read_inital_state()
    for day in range(80):
        update_lanternfishes(lanternfishes)

    # print(lanternfishes)
    print(sum(lanternfishes))

if __name__ == "__main__":
    main()
