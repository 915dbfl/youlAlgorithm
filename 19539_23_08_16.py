#23.08.16
#사과나무

n = int(input())
heights = list(map(int, input().split()))

if sum(heights) % 3 != 0:
    print("NO")
else:
    Max = sum(heights) //3
    for h in heights:
        Max -= h // 2

    if Max > 0:
        print("NO")
    else:
        print("YES")