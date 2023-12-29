import re
import numpy as np
import pandas as pd

with open('2023/input05', 'r') as inp:
    inputs = inp.read().splitlines()

mappings = re.findall('([a-z-]+)\s', '\n'.join(inputs))
seeds = np.array(re.findall('\d+', inputs[0]), dtype='int')

lines = [inputs.index(mapping+' map:') for mapping in mappings]
lines.append(len(inputs)+2)
mappings_dict = dict()
for i, mapping in enumerate(mappings):
    mat = np.array([line.split() for line in inputs[(lines[i]+1):(lines[i+1]-1)]], dtype='int')
    mappings_dict[mapping] = pd.DataFrame(mat, columns=['ds', 'ss', 'rl'])

# part 1 #
def source_to_dest(mapping_matrix, source):
    try:
        return (mapping_matrix
     .loc[lambda x: (x['ss']<=source) & (source<(x['ss']+x['rl']))]
     .assign(dest=lambda x: x['ds']-x['ss']+source)
     .loc[:, ['dest']]
     .values[0][0]
     )
    except:
        return source

def seed_to_location(seed, mappings_dict):
    source = seed
    for mapping in list(mappings_dict.keys()):
        destination = source_to_dest(mappings_dict[mapping], source)
        source = destination
    return destination

locations = []
for source in seeds:
    location = seed_to_location(source, mappings_dict)
    locations.append(location)

min(locations)

# part 2  - does not work #
starts = seeds[::2]
lengths = seeds[1::2]

closest_location = 999999999
for s, l in zip(starts, lengths):
    seed_gen = (s for s in range(s, s+l))
    for seed in seed_gen:
        location = seed_to_location(seed, mappings_dict)
        if location < closest_location:
            closest_location = location
