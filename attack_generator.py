import itertools

start_cost = 10

effects = {
    "area" : -2,
    "free action" : -3,
    "grapple" : -2,
    "restore" : -1,
    "status effect" : -1,
    "barrier" : -1,
    "teleportation" : -5,
    "drain" : 1,
    "long charge" : 2,
    "permanent" : 5,
    "rooted" :4,
    "unchargeable" : 3
}

# creates a list of the effect types
list = []
for key in effects:
    list.append(key)

# iterate through combinations, adding valid attacks with cost greater or equal to 1 to attacks list, or adding invalid attacks to invalids
attacks = []
invalids = []
for L in range(len(list) + 1):
    for subset in itertools.combinations(list, L):
        cost = start_cost
        for mod in subset:
            cost += effects[mod]
        if cost >= 1:
            attacks.append({subset : cost})
        else:
            invalids.append({subset : cost})

print(len(attacks))
print(len(invalids))
