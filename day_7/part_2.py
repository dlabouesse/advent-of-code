def read_inital_state():
    crabs_positions = []
    with open("input.txt", "r") as f:
        for line in f:
            for value in line.rstrip("\n").split(','):
                crabs_positions.append(int(value))
    return crabs_positions

def get_extremes_positions(crabs_positions):
    return (min(crabs_positions), max(crabs_positions))

def calculate_required_fuel(crabs_positions, target_position):
    required_fuel = 0
    for position in crabs_positions:
        n = abs(position-target_position)
        required_fuel += int(n*(1+n)/2)
    return required_fuel

def main():
    crabs_positions = read_inital_state()
    extremes_positions = get_extremes_positions(crabs_positions)
    required_fuel_for_each_position = {}
    for i in range(extremes_positions[0], extremes_positions[1]+1):
        required_fuel_for_each_position[i] = calculate_required_fuel(crabs_positions, i)

    cheapest_target_position = min(required_fuel_for_each_position, key=required_fuel_for_each_position.get)

    print('position: {}'.format(cheapest_target_position))
    print('required fuel: {}'.format(required_fuel_for_each_position[cheapest_target_position]))

if __name__ == "__main__":
    main()
