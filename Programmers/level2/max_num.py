#2022.03.30
#가장 큰 수

#내 풀이(오답)
def solution(numbers):
    numbers = list(str(i) for i in numbers)
    numbers.sort(key = lambda x: x[0], reverse = True)
    print(numbers)
    for i in range(len(numbers)-1):
        max = [numbers[i][0], i]
        for j in range(i, len(numbers)-1):
            if numbers[i] in numbers[j] and numbers[i] != numbers[j]:
                if int(numbers[j][len(numbers[i])]) > int(max[0]):
                    max[0] = numbers[j][len(numbers[i])]
                    max[1] = j
        tmp = numbers[i]
        numbers[i] = numbers[max[1]]
        numbers[max[1]] = tmp
    return ''.join(numbers)