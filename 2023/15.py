with open('2023/input15', 'r') as inp:
    input = inp.readline().strip('\n').split(',')

def HASH(sequence):
    current_value = 0
    for ch in sequence:
        current_value = ((current_value + ord(ch)) * 17) % 256
    return current_value

# part 1 #
sum_of_results = 0
for sequence in input:
    sum_of_results += HASH(sequence)

# part 2 #
import re

boxes = {num: {} for num in range(0, 256)}
for sequence in input:
    match = re.search(r'([a-z]+)(=|-)(\d?)', sequence)
    label, operation, focal_length = match.groups()
    if operation == '-':
        _ = boxes[HASH(label)].pop(label, '')
    if operation == '=':
        boxes[HASH(label)][label] = int(focal_length)

focusing_power = 0
for box, lenses in boxes.items():
    if len(lenses) == 0:
        continue
    for i, (lens, focal_length) in enumerate(lenses.items()):
        focusing_power += (box+1) * (i+1) * focal_length
