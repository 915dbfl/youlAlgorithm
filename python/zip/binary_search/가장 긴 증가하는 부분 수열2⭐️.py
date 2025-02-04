import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))

result = [a[0]]

def find_place(target):
    start = 0
    end = len(result) - 1

    while start <= end:
        mid = (start + end)//2

        if result[mid] < target:
            start = mid + 1
        elif result[mid] > target:
            start = mid - 1
        else:
            return mid
    return start

for item in a:
    if result[-1] < item:
        result.append(item)
    else:
        index = find_place(item)
        result[index] = item
print(len(result))