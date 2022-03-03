# 整数反转
# 给定一个整数，将其反转输出
# 如：输入123，输出321；输入120，输出21

# 需要注意负数的取余操作

import random


def reverse(num_in: int) -> int:
    if num_in < 0:
        neg = 1
    else:
        neg = 0
    num_out = 0
    num_in = abs(num_in)
    while num_in != 0:
        num_out = num_out * 10 + num_in % 10
        num_in = int(num_in/10)
    if neg == 1:
        num_out = -num_out
    if num_out > 2**31-1 or num_out < -2**31:
        num_out = 0
    return num_out


if __name__ == "__main__":
    k = random.randint(-2**31, 2**32)
    t = reverse(k)

    print(k, t)


