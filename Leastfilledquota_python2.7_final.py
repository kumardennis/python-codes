# Fills the least filled quotas randomly.
# Seperates the prioritized brands from the list of all brands and returns desired results.
from itertools import groupby
import random
from operator import itemgetter
from collections import OrderedDict


# Make dictionary
quotas = {
    "brand a" : (20, 20, 0), #priority
    "brand b" : (0, 20, 0),
    "brand c" : (0, 20, 0),
    "brand d" : (20, 20, 0), #priority
    "brand e" : (0, 20, 0),
    "brand f" : (0, 20, 0),
    "brand g" : (0, 20, 0),
    "brand h" : (0, 20, 0),
    "brand i" : (20, 20, 0), #priority
    "brand j" : (20, 20, 0),
    "brand k" : (20, 20, 0), #priority
    "brand l" : (0, 20, 0),
    "brand n" : (0, 20, 0),
    "brand o" : (0, 20, 0),
}




def LeastFilledRandomQuota(non_priority, prio,quotaFull,num1, priority, num2, maximumQuota):




    def quotaSplit(array):
        # global dict
        quotaWhole = quotaFull.copy()
        indices = []
        for i in range(len(array)):
            itemKey = quotaFull.keys()
            itemKeyAdd = list(itemKey)[array[i]-1]
            itemValue = quotaFull.values()
            itemValueAdd = list(itemValue)[array[i]-1]

            if itemValueAdd[0] != maximumQuota:
                priority[itemKeyAdd] = itemValueAdd
                indices.append(itemKeyAdd)
        print("value",priority)

        nonprio = []
        for i in range(len(quotaWhole)):
            nonprio.append(i+1)

        for i in range(len(array)):
            nonprio.remove(array[i])

        indices2 = []
        for i in range(len(nonprio)):
            itemKey2 = quotaFull.keys()
            itemKeyAdd2 = list(itemKey2)[nonprio[i]-1]
            itemValue2 = quotaFull.values()
            itemValueAdd2 = list(itemValue2)[nonprio[i]-1]
            if itemValueAdd2[0] != maximumQuota:
                non_priority[itemKeyAdd2] = itemValueAdd2
                indices2.append(itemKeyAdd2)
        # print(indices2)

        # print("nontest", nonprio)
        # print("prio",priority)
        # print("non-prio",non_priority)
        return priority, non_priority


    # Select FOUR from other quotas
    def leastFilledQuota(quota, num):
        # global dict
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
            dicting = dict(finalArr)
            # print("quota to show",dict)
            return dicting
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




    quotaSplit(prio)
    allFull = 0
    allFull = len(priority)
    allFull2 = len(non_priority)
    print("allfull",allFull)

    non_prio_quotas = leastFilledQuota(non_priority,num1)
    difference = 0
    if allFull == 0:
        # prio_quotas = leastFilledQuota(priority, num2)
        non_prio_quotas = leastFilledQuota(non_priority,(num1+num2))
        print("cond 3")
    elif num2 > allFull:
        difference = num2 - allFull
        print("diff", difference)
        non_prio_quotas = leastFilledQuota(non_priority,(num1+difference))
        prio_quotas = leastFilledQuota(priority, (num2 - difference))
        print("cond 1")
    elif num2 <= allFull:
        prio_quotas = leastFilledQuota(priority, num2)
        non_prio_quotas = leastFilledQuota(non_priority,num1)
        print("cond 2")
    elif num1 <= allFull2:
        diff2 = allFull2 - num1
        non_prio_quotas = leastFilledQuota(non_priority,(num1-difference))


    if allFull == 0:
        merged = non_prio_quotas
    else:
        merged = merge_two_dicts(non_prio_quotas,prio_quotas)


    # print(prio_quotas)
    # print(non_prio_quotas)
    # print("merged",merged)
    # print("Brands:", merged.keys())
    # print(priority["brand a"][0])
    return merged.keys()


priority = {}
non_priority = {}

#LeastFilledRandomQuota([Brands to be prioritized], non-priority quotas, number of random brands needed from non-prio, prioritized quota, Number of random brands from priority quota)

print(LeastFilledRandomQuota(non_priority, [1,4,9,11],quotas, 4, priority,3, 20))
