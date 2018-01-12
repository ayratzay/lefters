from random import choices, shuffle, choice, normalvariate
from handler import epoch


TFR = 2.36
TFD = 1

initial_left_ratio = 0
initial_pop_males = 200000
initial_pop_females = 200000

pm = choices(population=['r', 'l'], weights=[1-initial_left_ratio, initial_left_ratio], k=initial_pop_males)
pf = choices(population=['r', 'l'], weights=[1-initial_left_ratio, initial_left_ratio], k=initial_pop_females)

ratios = []
population = []
for i in range(20):
    print(i)
    pm, pf = epoch(pm, pf, TFR, TFD)
    rm = pm.count('l') / float(len(pm))
    rf = pf.count('l') / float(len(pf))
    ratios.append((rm, rf))
    population.append(len(pm) + len(pf))