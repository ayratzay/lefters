from random import choice, choices, normalvariate, shuffle

def kids_destiny(m, f):
    if m=='l':
        if f=='l':
            return 0.24
        elif f=='r':
            return 0.17
    elif m=='r':
        if f=='l':
            return 0.22
        elif f=='r':
            return 0.09


def hand(left_ratio):
    return choices(population=['r', 'l'], weights=[1-left_ratio, left_ratio])[0]


def gender():
    return choice(['m', 'f'])


def kid(m, f):
    left_ratio = kids_destiny(m, f)
    return gender(), hand(left_ratio)


def form_next_gen(m, f, fert):
    mp = []
    fp = []
    for i in range(fert):
        g, h = kid(m, f)
        if g == 'm':
            mp.append(h)
        else:
            fp.append(h)
    return mp, fp


def family(m, f, TFR, TFD):
    nkids = int(normalvariate(TFR, TFD))
    return form_next_gen(m, f, nkids)


def epoch(pm, pf, TFR, TFD):
    new_gen_pm = []
    new_gen_pf = []

    shuffle(pm)
    shuffle(pf)

    for m, f in zip(pm, pf):
        fmp, ffp = family(m, f, TFR, TFD)
        new_gen_pm += fmp
        new_gen_pf += ffp

    return new_gen_pm, new_gen_pf