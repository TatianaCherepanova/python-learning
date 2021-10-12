import bisect_left, bisect_right

def filter_less_five(lst):
	result = []
	for element in lst:
		if element < 5:
			result.append(element) 
	return result


a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
b = [1, 1, 2, 3]

assert filter_less_five(a) == b
assert filter_less_five(b) == b
assert filter_less_five([]) == []
assert filter_less_five([5, 5, 5]) == []
assert filter_less_five([1, 2, 1, 2]) == [1, 2, 1, 2]
assert filter_less_five([1, 6, 2, 6, 3, 7, 4, 8, 5]) == [1, 2, 3, 4]
assert filter_less_five([-5, 0, -6, 6, -7, 7, -8]) == [-5, 0, -6, -7, -8]

print(filter_less_five(a))


def common_elements(lst1, lst2):
	lst1.sort()
	lst2.sort()
	if len(lst2) < len(lst1):
		lst1, lst2 = lst2, lst1
	idx = 0
	while idx < len(lst1):
		// 1) найти кол-во элементов lst1[idx] в списке lst1
		// 2) найти количество элементов в lst1[idx] в списке lst2
		// добавить в результирующий список min[1), 2)] элементов lst1
		// сместить индекс на 1)
		idx = idx + 1
	// вернуть результат


b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

assert common_elements([], []) == []
assert common_elements([1], []) == []
assert common_elements([1, 1], []) == []
assert common_elements([], [1]) == []
assert common_elements([], [1, 1]) == []
assert common_elements([1],[2]) == []
assert common_elements([1, 2], [2]) == [2]
assert common_elements([2], [1, 2]) == [2]
assert common_elements([1, 2], [2, 1]) == [1, 2]
assert common_elements([1, 1, 2], [2, 1, 1]) == [1, 1, 2]
assert common_elements([1, 1, 2], [2, 1]) == [1, 2]
assert common_elements([2, 1], [1, 1, 2]) == [2, 1]
assert common_elements([1, 1, 1], [1]) == [1]
assert common_elements([1, 1, 1], [1, 1]) == [1, 1]
assert common_elements([1], [1, 1, 1]) == [1]
assert common_elements([1, 1], [1, 1, 1]) == [1, 1]
assert common_elements([1, 1, 2, 2, 2], [2, 2, 1, 1, 1]) == [1, 1, 2, 2]