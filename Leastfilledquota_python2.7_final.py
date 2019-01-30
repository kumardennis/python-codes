# Fills the least filled quotas randomly.
# Seperates the prioritized brands from the list of all brands and returns desired results.
from itertools import groupby
import random
from operator import itemgetter
from collections import OrderedDict


# Make dictionary
quotas = {
    "brand a" : (0, 20, 0), #priority
    "brand b" : (0, 20, 0), #priority
    "brand c" : (0, 20, 0), #priority
    "brand d" : (0, 20, 0), #priority
    "brand e" : (0, 20, 0),
    "brand f" : (0, 20, 0),
    "brand g" : (0, 20, 0),
    "brand h" : (0, 20, 0),
    "brand i" : (0, 20, 0),
    "brand j" : (0, 20, 0),
    "brand k" : (0, 20, 0),
    "brand l" : (0, 20, 0),
    "brand n" : (0, 20, 0),
    "brand o" : (0, 20, 0),
}




def LeastFilledRandomQuota(prio,quotaFull,num1, priority, num2):




    def quotaSplit(array):
        # global dict
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

        # print(priority)
        return priority


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
    non_prio_quotas = leastFilledQuota(quotaFull,num1)
    prio_quotas = leastFilledQuota(priority, num2)
    merged = merge_two_dicts(non_prio_quotas,prio_quotas)
    # print("merged",merged)
    # print("Brands:", merged.keys())
    return merged.keys()

quotaWhole = quotas.copy()
priority = {}

#LeastFilledRandomQuota([Brands to be prioritized], non-priority quotas, number of random brands needed from non-prio, prioritized quota, Number of random brands from priority quota)

print(LeastFilledRandomQuota([1,2,3,4],quotas, 4, priority, 2))
