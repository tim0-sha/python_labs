def transpose(mat: list[list[float | int]]) -> list[list]:
    if mat == []:
        return []
    stroka = len(mat[0])
    for i in mat:
        if len(i) != stroka: 
            raise ValueError("рваная матрица")
    stolb = len(mat)
    answer = [[0 for i in range(stolb)] for j in range(stroka)]
    for i in range(stolb):
        for j in range(stroka):
            answer[j][i] = mat[i][j]
    return answer
"""
print(transpose([[1, 2, 3]]))
print(transpose([[1], [2], [3]]))
print(transpose([[1, 2], [3, 4]]))
print(transpose([]))
print(transpose([[1, 2], [3]]))
"""
def row_sums(mat: list[list[float | int]]) -> list[float]:
    if (mat == []) or (mat ==[[]]):
        raise ValueError("пустая матрица")
    for i in mat:
        if len(i) != len(mat[0]): 
            raise ValueError("рваная")
    answer = []
    for i in mat:
        answer.append(sum(i))
    return answer
"""
print(row_sums([[1, 2, 3], [4, 5, 6]]))
print(row_sums([[-1, 1], [10, -10]]))
print(row_sums([[0, 0], [0, 0]]))
print(row_sums([[1, 2], [3]]))
"""
def col_sums(mat: list[list[float | int]]) -> list[float]:
    for i in mat:
        if len(i) != len(mat[0]): 
            raise ValueError("рваная")
    mat = transpose(mat)
    return row_sums(mat)
"""
print(col_sums([[1, 2, 3], [4, 5, 6]]))
print(col_sums([[-1, 1], [10, -10]]))
print(col_sums([[0, 0], [0, 0]]))
print(col_sums([[1, 2], [3]]))
"""