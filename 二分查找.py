
import random


# 二分查找，需要lst从小到大排序
def bin_search(lst, target):
    i = 0
    j = len(lst)-1
    while i <= j:
        mid = int((i+j)/2)
        if target == lst[mid]:
            return mid
        elif target > lst[mid]:
            i = mid
        else:
            j = mid
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
