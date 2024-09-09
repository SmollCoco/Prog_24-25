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


def iterMergeSort(l: list) -> list:
    all_ = [[i] for i in l]

    while len(all_) > 1:
        all_.append(merge(all_.pop(0), all_.pop(0)))

    return all_[0] if all_ else []


ll = [6, 75, 20, 88, 19]
print(iterMergeSort(ll))
