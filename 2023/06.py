import numpy as np

# part 1 #
times = [42, 89, 91, 89]
distances = [308, 1170, 1291, 1467]

cnts = []
for t, d in zip(times, distances):
    coefficients = [-1, t, -d]
    solutions = np.roots(coefficients)
    start = np.ceil(min(solutions))
    end = np.floor(max(solutions))
    cnts.append(end - start + 1)

product = 1
for c in cnts:
    product *= c

# part 2 #
time = 42899189
distance = 308117012911467
coefficients = [-1, time, -distance]
solutions = np.roots(coefficients)
start = np.ceil(min(solutions))
end = np.floor(max(solutions))
print(end - start + 1)
