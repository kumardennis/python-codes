# Fills the least filled quotas randomly.
# Seperates the prioritized brands from the list of all brands and returns desired results.
from itertools import groupby
import random
from operator import itemgetter
from collections import OrderedDict


# Make dictionary
quotaFull = {
    "brand b" : (1, 20, 0),
    "brand a" : (1, 20, 0), #priority
    "brand c" : (2, 20, 0),
    "brand d" : (3, 20, 0),
    "brand e" : (1, 20, 0), #priority
    "brand f" : (3, 20, 0),
    "brand g" : (4, 20, 0),
    "brand h" : (7, 20, 0),
    "brand i" : (3, 20, 0),
    "brand j" : (4, 20, 0), #priority
    "brand k" : (5, 20, 0),
    "brand l" : (2, 20, 0), #priority
}

quotaWhole = quotaFull.copy()

# item = quotaFull.values()
# def LeastFillPrio(prio, quota, num1, num2):

priority = {}
non_priority = {}

def quotaSplit(array):
    global dict
    indices = []
    for i in range(len(array)):
        itemKey = quotaFull.keys()
        itemKeyAdd = list(itemKey)[array[i]-1]
        itemValue = quotaFull.values()
        itemValueAdd = list(itemValue)[array[i]-1]
        priority[itemKeyAdd] = itemValueAdd
        indices.append(itemKeyAdd)

    for i in range(len(indices)):
        item = indices[i]
        if item == list(priority.keys())[i]:
            del quotaFull[item]
        else:
            print("test")

    print(priority)
    return priority


# Select FOUR from other quotas
def leastFilledQuota(quota, num):
    global dict
    sort_quota1 = {}
    sort_quota = {}
    dict_sort_quota = {}
    sort_quota1 = sorted(quota.values())
    # print("sort quota 1", sort_quota1)
    dups = [len(list(group)) for key, group in groupby(sort_quota1)]
    # print("dups", dups)
    sort_quota = sorted(quota.items(), key=itemgetter(1))
    dict_sort_quota = dict(sort_quota)
    dict_sort_quota = OrderedDict(sorted(dict_sort_quota.items(), key=itemgetter(1)))

    if dups[0] >= num:
        limit = dups[0]
        finalArr = []
        randome = random.sample(range(0, limit), num)
        # print("randome ",randome)
        for j in range(num):
            # print(randome)
            finalArr.append(sort_quota[randome[j]])
            # print("brand name ",list(sort_quota)[randome[j]])
        dict = dict(finalArr)
        # print("quota to show",dict)
        return dict
    elif dups[0] < num:
        finalArr = []
        helperFinal = []
        sum1 = 0
        for i in range(len(dups)):
            sum1 = sum1 + dups[i]
            # print("index of stop", i)
            if dups[i] < num and sum1 < num:
                # print("dupsand num ",dups[i], num)
                helperFinal.append(dups[i])
            else:
                index=i
                break
        # print("helper: ",helperFinal)

        for i in range(sum(helperFinal)):
            finalArr.append(sort_quota[i])
        # print("finalarr ", finalArr)
        bum = len(finalArr)
        randome = random.sample(range(sum(helperFinal), sum(helperFinal)+dups[index]), num-sum(helperFinal))
        randome.sort()
        # print("randome ", randome)
        # print("bum ", bum)
        for j in range(num-sum(helperFinal)):
            # print(randome[j])
            finalArr.append(sort_quota[randome[j]])
            # print("brand name ",sort_quota[randome[j]])
        dictionary = dict(finalArr)
        dictionary = OrderedDict(sorted(dictionary.items(), key=itemgetter(1)))
        # print("quotas to show", dictionary)
        return dictionary

def merge_two_dicts(x,y):
    merge = x.copy()
    merge.update(y)
    merge = OrderedDict(sorted(merge.items(), key=itemgetter(1)))
    return merge


def LeastFilledRandomQuota(prio,quotaFull,num1, priority, num2):
    quotaSplit(prio)
    non_prio_quotas = leastFilledQuota(quotaFull,num1)
    prio_quotas = leastFilledQuota(priority, num2)
    merged = merge_two_dicts(non_prio_quotas,prio_quotas)
    print("merged",merged)
    print("Brands:", merged.keys())

LeastFilledRandomQuota([1,4,9,11],quotaFull, 4, priority, 2)
