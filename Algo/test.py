def merge(L1, L2):
    index, index2 = 0, 0
    L3 = []
    while index < len(L1) and index2 < len(L2):
        if L1[index] < L2[index2]:
            L3.append(L1[index])
            index += 1
        else:
            L3.append(L2[index2])
            index2 += 1
    while index < len(L1):
        L3.append(L1[index])
        index += 1
    while index2 < len(L2):
        L3.append(L2[index2])
        index2 += 1
    return L3


# print(merge([3, 4, 8, 19, 46, 67], [5, 7, 10, 40, 42, 50, 65]))


def merge_sort(l):
    if len(l) <= 1:
        return l

    l1 = merge_sort(l[: len(l) // 2])
    l2 = merge_sort(l[len(l) // 2 :])

    return merge(l1, l2)


ll = [6, 75, 20, 88, 19]
print(merge_sort(ll))

""" notion de classe de compléxité """
# on qualifie de qualitative, tout amelioration de solution qui deminue la classe de compléxité


def iterMergeSort(l: list) -> list:
    if not l:
        return l

    all_ = [[i] for i in l]

    while len(all_) > 1:
        print(*all_)
        all_.append(merge(all_.pop(0), all_.pop(0)))

    print(*all_)
    return all_[0]


print(iterMergeSort(ll))
