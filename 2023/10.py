import numpy as np

# part 1 #
with open('2023/input10', 'r') as inp:
    inputs = inp.read().splitlines()

for i, line in enumerate(inputs):
    try:
        index = line.index('S')
        break
    except:
        pass

pipes = {'|': 'NS', '-': 'EW', 'L': 'NE', 'J': 'NW', '7': 'SW', 'F': 'SE'}
directions = {'N': [0, -1], 'S': [0, +1], 'E': [+1, 0], 'W': [-1, 0]}
head_to_arrive = {'N': 'S', 'E': 'W', 'S': 'N', 'W': 'E'}
start = np.array([index, i])
moves = 1
pos = np.array([index, i-1])
arriving = 'S'
tile = '|'

while tile != 'S':
    heading = pipes[tile].replace(arriving, "")
    pos += directions[heading]
    moves += 1
    tile = inputs[pos[1]][pos[0]]
    arriving = head_to_arrive[heading]

