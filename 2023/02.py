import re

# part 1 #
max_cubes = [12, 13, 14]
sum_of_possible_games = 0
game = 0
with open('2023/input02', 'r') as inp:
    while True:
        line = inp.readline()
        if not line:
            break
        game += 1
        red_max = max([int(r) for r in re.findall('(\d+) red', line)])
        green_max = max([int(r) for r in re.findall('(\d+) green', line)])
        blue_max = max([int(r) for r in re.findall('(\d+) blue', line)])
        game_max = [red_max, green_max, blue_max]
        if all([m <= n for m, n in zip(game_max, max_cubes)]):
            sum_of_possible_games += game

# part 2 #
sum_of_sets = 0
with open('2023/input02', 'r') as inp:
    while True:
        line = inp.readline()
        if not line:
            break
        red_max = max([int(r) for r in re.findall('(\d+) red', line)])
        green_max = max([int(r) for r in re.findall('(\d+) green', line)])
        blue_max = max([int(r) for r in re.findall('(\d+) blue', line)])
        sum_of_sets += red_max * green_max * blue_max
