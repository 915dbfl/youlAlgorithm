# 기출 문제
n = input()
nums = []

for i in n:
    nums.append(int(i))

mid = len(nums)//2
if sum(nums[:mid]) == sum(nums[mid:]):
    print("LUCKY")
else:
    print("READY")