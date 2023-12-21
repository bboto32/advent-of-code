import re


def extract_numbers(line):
    matches1 = re.search(r':(.*?)\|', line)
    matches2 = re.search(r'\|(.*?)$', line)
    return [int(i) for i in matches1.group(1).split()], [int(i) for i in matches2.group(1).split()]


# part 1 #
total_points = 0
with open('2023/input04', 'r') as inp:
    while True:
        line = inp.readline()
        if not line:
            break
        winning_numbers, my_numbers = extract_numbers(line)
        matches = [1 for i in my_numbers if i in winning_numbers]
        if matches:
            total_points += 2**(len(matches)-1)

# part 2 #
original_cards = 0
cards = {num: 1 for num in range(1, 202)}
with open('2023/input04', 'r') as inp:
    while True:
        line = inp.readline()
        if not line:
            break
        original_cards += 1
        winning_numbers, my_numbers = extract_numbers(line)
        matches = [original_cards+1 for i in my_numbers if i in winning_numbers]
        for i in [sum(x) for x in zip(matches, [*range(0,len(matches))])]:
            cards[i] += cards[original_cards]

n_cards = sum(cards.values())