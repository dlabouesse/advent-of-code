import tools.readfile as readfile

def move_probe(position, speed):
    position[0] += speed['x']
    position[1] += speed['y']
    if (speed['x'] > 0):
        speed['x'] -= 1
    elif (speed['x'] < 0):
        speed['x'] += 1
    speed['y'] -= 1

def launch_probe(target):
    speed = {
        'x' : 1,
        'y' : 1
    }
    max_y  = 0

    # vertical speed above max_x would require : 0 < speed['x'] < 1.
    for y_speed in range(target['min_y'], target['max_x']):
        for x_speed in range(1, target['max_x']+1):
            speed['x'] = x_speed
            speed['y'] = y_speed
            position = [0, 0]
            current_max_y = 0
            while True:
                move_probe(position, speed)
                current_max_y = max(current_max_y, position[1])
                if (position[0] > target['max_x'] or position[1] < target['min_y']):
                    break
                elif (speed['x'] == 0 and (position[0] < target['min_x'] or position[0] > target['max_x'])):
                    break
                elif (position[0] >= target['min_x'] and position[0] <= target['max_x'] and  position[1] >= target['min_y'] and position[1] <= target['max_y']):
                    # print('Target reached! :  ({}, {}) position when launching at x: {}, y: {}.'.format(position[0],  position[1], x_speed, y_speed))
                    max_y = max(max_y, current_max_y)
    return max_y

def main():
    ##### Sample #####
    # target  = {
    #     'min_x': 20,
    #     'max_x': 30,
    #     'min_y': -10,
    #     'max_y': -5
    # }

    ##### Input #####
    target  = {
        'min_x': 111,
        'max_x': 161,
        'min_y': -154,
        'max_y': -101
    }

    print(launch_probe(target))

if __name__ == "__main__":
    main()
