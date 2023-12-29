import pandas as pd

with open('2023/input08', 'r') as inp:
    instructions = inp.readline().strip('\n')

network = pd.read_csv('2023/input08', engine='python', skiprows=2,  sep=' =', header=None, names=['node', 'L'])
network[['L', 'R']] = network['L'].str.extract(r'\((\w+), (\w+)\)')
network = network.set_index('node')

# part 1 #
origin = 'AAA'
destination = 'AAA'
step = 0
ins_l = len(instructions)
while destination != 'ZZZ':
    destination = network.loc[origin].loc[instructions[step%ins_l]]
    origin = destination
    step += 1


# part 2 - does not work #
network = (network
           .reset_index()
           .assign(letter=lambda x: x.apply(lambda row: row['node'][2], axis=1))
           .set_index('node')
)

origins = network.loc[network.letter=='A']
destinations = origins
step = 0
ins_l = len(instructions)
while (destinations.letter=='Z').sum()!=len(destinations):
    destinations = network.loc[origins.loc[:, instructions[step%ins_l]]]
    origins = destinations
    step += 1
    if step % 5000 == 0:
        print(step)
