f = open("input.txt", "r")
previous_line = None
deltas = {"increased": 0, "decreased": 0, "same": 0, "other": 0}
values = []
for line in f:
    values.append(int(line))

previous_sum_values = None
for i in range(len(values)-2):
    current_sum_values = values[i] + values[i+1] + values [i+2]
    if previous_sum_values:
        if int(current_sum_values) > int(previous_sum_values):
            deltas["increased"] += 1
        elif int(current_sum_values) < int(previous_sum_values):
            deltas["decreased"] += 1
        elif int(current_sum_values) == int(previous_sum_values):
            deltas["same"] += 1
        else:
            deltas["other"] += 1

    previous_sum_values = current_sum_values

print(deltas)
