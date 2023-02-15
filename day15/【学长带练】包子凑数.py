from math import gcd


N = 100 * 100

dp = [0] * N
dp[0] = 1


def count(nums):
    for i in range(N):
        if dp[i]:

            for n in nums:
                k = i + n

                if k < N:
                    dp[k] = 1

    return dp.count(0)


if __name__ == '__main__':
    nums = [int(input()) for _ in range(int(input()))]

    d = 0
    for i in nums:
        d = gcd(d, i)

    print('INF' if d > 1 else count(nums))