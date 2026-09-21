def min_max(nums: list[float | int]) -> tuple[float | int, float | int]:
    if len(nums) == 0:
        raise ValueError("список пуст")
    lo = nums[0]
    mx = nums[0]
    for i in nums:
        if i < lo:
            lo = i
        elif i > mx:
            mx = i
    return (lo, mx)
"""
print(min_max([3, -1, 5, 5, 0]))
print(min_max([42]))
print(min_max([-5, -2, -9]))
print(min_max([1.5, 2, 2.0, -3.1]))
print(min_max([]))
"""
def unique_sorted(nums: list[float | int]) -> list[float | int]:
    nums = sorted(set(nums))
    return nums
"""
print(unique_sorted([3, 1, 2, 1, 3]))
print(unique_sorted([]))
print(unique_sorted([-1, -1, 0, 2, 2]))
print(unique_sorted([1.0, 1, 2.5, 2.5, 0]))
"""
def flatten(mat: list[list | tuple]) -> list:
    answer = []
    for i in mat:
        if (type(i) == list) or (type(i) == tuple):
            answer += i
        else: 
            raise TypeError ("строка не строка строк матрицы")
    return answer

print(flatten([[1, 2], [3, 4]]))
print(flatten([[1, 2], (3, 4, 5)]))
print(flatten([[1], [], [2, 3]]))
print(flatten([[1, 2], "ab"]))
