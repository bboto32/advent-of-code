import numpy as np

# part 1 #
def extrapolate(line):
    nv = line[-1][-1]
    while any(line[-1] != 0):
        line.append(line[-1][1:] - line[-1][:-1])
        nv += line[-1][-1]
    return nv


sum_of_values = 0
with open('2023/input09', 'r') as inp:
    while True:
        line = inp.readline().strip('\n')
        if not line:
            break
        line = [np.array([int(i) for i in line.split()])]
        sum_of_values += extrapolate(line)

# part 2 #
def extrapolate_backwards(line):
    nv = line[-1][0]
    i = 1
    while any(line[-1] != 0):
        line.append(line[-1][1:] - line[-1][:-1])
        i += 1
        nv += (-1 if i % 2 == 0 else 1) * line[-1][0]
    return nv


sum_of_values = 0
with open('2023/input09', 'r') as inp:
    while True:
        line = inp.readline().strip('\n')
        if not line:
            break
        line = [np.array([int(i) for i in line.split()])]
        sum_of_values += extrapolate_backwards(line)
