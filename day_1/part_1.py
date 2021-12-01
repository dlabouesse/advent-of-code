f = open("input.txt", "r")
previous_line = None
deltas = {"increased": 0, "decreased": 0, "same": 0, "other": 0}
for line in f:
    if previous_line:
        if int(line) > int(previous_line):
            deltas["increased"] += 1
        elif int(line) < int(previous_line):
            deltas["decreased"] += 1
        elif int(line) == int(previous_line):
            deltas["same"] += 1
        else:
            deltas["other"] += 1
    previous_line = line

print(deltas)
