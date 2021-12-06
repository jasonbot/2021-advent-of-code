import collections


def downtick(item):
    if item > 0:
        return item - 1
    else:
        return 6


def tick(lfa):
    babies = sum(1 for item in lfa if item == 0)
    next_tick = [downtick(item) for item in lfa] + ([8] * babies)
    return next_tick


def smarter_tick(lfd):
    next_dict = {(k - 1): v for k, v in lfd.items()}
    if -1 in next_dict:
        babies = next_dict[-1]
        if 6 not in next_dict:
            next_dict[6] = 0
        next_dict[6] += babies
        del next_dict[-1]
        next_dict[8] = next_dict.get(8, 0) + babies
    return next_dict


lfa = [int(item) for item in open("day6.txt").read().split(",")]
print(lfa)
lfd = collections.defaultdict(int)
for item in lfa:
    lfd[item] += 1

for days in range(80):
    lfa = tick(lfa)

print(lfa, len(lfa))

for days in range(256):
    lfd = smarter_tick(lfd)
print(lfd, days)

print(sum(lfd.values()))