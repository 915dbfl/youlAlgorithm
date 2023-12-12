# 2차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree1(a):
    n = len(a) # 행 길이 계산
    m = len(a[0]) # 열 길이 계산
    result = [[0] * n for _ in range(m)] # 결과 리스트
    for i in range(n):
        for j in range(m):
            result[j][n - i - 1] = a[i][j]
    return result

# 다차원 리스트 90도 회전
def rotate_a_matrix_by_90_degree2(a):
    return list(zip(*a[::-1]))

'''
[input example]
[[0, 0, 0], [1, 0, 0], [0, 1, 1]]
[output example]
[[0, 1, 0], [1, 0, 0], [1, 0, 0]]
'''