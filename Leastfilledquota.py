# Least filled quotas thing.
from itertools import groupby
import random


# Make dictionary

quota = {
    "brand b" : (1, 20, 0),
    "brand c" : (2, 20, 0),
    "brand d" : (3, 20, 0),
    "brand f" : (3, 20, 0),
    "brand g" : (4, 20, 0),
    "brand h" : (7, 20, 0),
    "brand i" : (3, 20, 0),
    "brand j" : (4, 20, 0),
    "brand k" : (5, 20, 0),
    "brand l" : (2, 20, 0),
}


quota_prio = {
    "brand a" : (1, 20, 0),
    "brand e" : (1, 20, 0),
    "brand j" : (1, 20, 0),
    "brand f" : (2, 20, 0)
}

# Select ONE from priority quota
sort_quota_prio1 = sorted(quota_prio.values())
dups_prio = [len(list(group)) for key, group in groupby(sort_quota_prio1)]

sort_quota_prio = sorted(quota_prio.items(), key=lambda x:x[1])
dict_sort_quota_prio = dict(sort_quota_prio)
# print(sort_quota_prio)
# print(dict_sort_quota_prio)

# print(dups_prio)


limit_prio = dups_prio[0]
# print(limit_prio)
randome_prio = random.randint(0, limit_prio-1)
# print(randome_prio)

brand_to_show_prio = list(sort_quota_prio)[randome_prio]
# print(brand_to_show_prio)

finalArr_prio = []

finalArr_prio.append(brand_to_show_prio)
# print(finalArr)
dict_prio = dict(finalArr_prio)
print(dict_prio)


# Select FOUR from other quotas
sort_quota1 = sorted(quota.values())
print("sort quota 1", sort_quota1)
dups = [len(list(group)) for key, group in groupby(sort_quota1)]
print("dups", dups)

sort_quota = sorted(quota.items(), key=lambda x:x[1])
dict_sort_quota = dict(sort_quota)
# print(sort_quota)
print("sort quota dict",dict_sort_quota)

num = 5




if dups[0] >= num:
    limit = dups[0]
    finalArr = []
    randome = random.sample(range(0, limit), num)
    # print("randome ",randome)
    for j in range(num):
        # print(randome)
        finalArr.append(list(sort_quota)[randome[j]])
        # print("brand name ",list(sort_quota)[randome[j]])
    dictionary = finalArr
    print(dict)
elif dups[0] < num:
    finalArr = []
    helperFinal = []
    sum1 = 0
    for i in range(len(dups)):
        sum1 = sum1 + dups[i]
        if dups[i] < num and sum1 < num:
            print("dupsand num ",dups[i], num)
            helperFinal.append(dups[i])
        else:
            print("index of stop", i)
            index=i
            break
    print("helper: ",helperFinal)

    for i in range(sum(helperFinal)):
        finalArr.append(list(sort_quota)[i])
    print("finalarr ", finalArr)
    bum = len(finalArr)
    randome = random.sample(range(sum(helperFinal), sum(helperFinal)+dups[index]), num-sum(helperFinal))
    randome.sort()
    print("randome ", randome)
    print("bum ", bum)
    for j in range(num-sum(helperFinal)):
        # print(randome[j])
        finalArr.append(list(sort_quota)[randome[j]])
        # print("brand name ",list(sort_quota)[randome[j]])
    dictionary = finalArr
    print(dictionary)

print("numbumdiff ",abs(num-bum))

def merge_two_dicts(x,y):
    merge = x.copy()
    merge.update(y)
    return merge

# print("final dict ",merge_two_dicts(dict_prio, dict))
