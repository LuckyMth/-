
import random


# 二分查找，需要lst从小到大排序
def bin_search(lst, ni):
    bsi = 0
    bsj = len(lst)-1
    while bsi != bsj:
        bm = int((bsi+bsj)/2)
        if ni == lst[bm]:
            return bm
        elif ni > lst[bm]:
            bsi = bm
        else:
            bsj = bm
    return -1


if __name__ == "__main__":
    k = 20
    arr = []
    while k != 0:
        while 1:
            tem = random.randint(0, 1000)
            if tem not in arr:
                arr.append(tem)
                break
        k = k-1
    arr.sort()
    t = bin_search(arr, arr[13])
    print(t)
