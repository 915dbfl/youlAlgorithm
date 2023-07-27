#민균이의 계략
#dp

#n^2
n = int(input())
nums = list(map(int, input().split()))
dp = [1] * n

for i in range(1, n):
    for j in range(i):
        if nums[i] > nums[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(max(dp))

#이분탐색
n = int(input())
nums = list(map(int, input().split()))

def binary_search(arr, target):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] >= target:
            right = mid - 1
        else:
            left = mid + 1
    return left

lis = []

#nlogn
for num in nums:
    # 이분 탐색으로 위치 파악 후 삽입
    idx = binary_search(lis, num)
    if idx == len(lis):
        lis.append(num)
    else:
        lis[idx] = num

print(len(lis))