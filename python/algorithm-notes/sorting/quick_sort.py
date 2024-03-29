# 퀵 정렬
# 최선: O(nlogn) / 최악: O(n^2)
# 피벗을 사용
# 데이터가 무작위로 입력될 경우, 빠르게 동작
# 리스트의 첫 번째 요소가 피벗으로 지정될 경우, 이미 데이터가 정렬되어 있다면 매우 느리게 동작

# 정석 알고리즘
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort1(array, start, end):
    if start >= end: # 원소가 1개인 경우 종료
        return
    
    pivot = start # 피벗은 첫 번째 요소
    left = start + 1
    right = end

    while left <= right:
        # 피벗보다 큰 데이터를 찾을 때까지 반복
        while (left <= end and array[left] <= array[pivot]):
            left += 1
        # 피벗보다 작은 데이터를 찾을 때까지 반복
        while (right > start and array[start] >= array[pivot]):
            right -= 1
        if left > right: # 엇갈렸다면 작은 데이터와 피벗을 교체
            array[right], array[pivot] = array[pivot], array[right]
        else: # 엇갈리지 않았다면 작은 데이터와 큰 데이터를 교체
            array[left], array[right] = array[right], array[left]
    
    # 분할 이후 왼쪽 부분과 오른 쪽 부분에서 각각 정렬 수행
    quick_sort1(array, start, right -1)
    quick_sort1(array, right + 1, end)

quick_sort1(array, 0, len(array)-1)
print(array)

# 더 짧지만 비교 연산 증가로 더 비효율적인 알고리즘
def quick_sort2(array):
    # 리스트가 하나 이하의 원소만을 담고 있다면 종료
    if len(array) <= 1:
        return array
    
    pivot = array[0] # 피벗은 첫 번째 원소
    tail = array[1:] # 피벗을 제외한 리스트

    left_side = [x for x in tail if x <= pivot] # 분할된 왼쪽 부분
    right_side = [x for x in tail if x > pivot] # 분할된 오른쪽 부분

    # 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고, 전체 리스트를 반환
    return quick_sort2(left_side) + [pivot] + quick_sort2(right_side)

print(quick_sort2(array))