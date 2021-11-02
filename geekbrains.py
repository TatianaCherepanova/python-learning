from bisect import bisect_left, bisect_right

# Задача 1

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

# Задача 2

def common_elements(lst1, lst2):
	# Функция принимает две последовательности (списка) 
	# и возвращает отсортированный список общих элементов

	lst1.sort()
	lst2.sort()
	result = []
	
	if len(lst2) < len(lst1):
		lst1, lst2 = lst2, lst1    # меняем списки местами
	
	assert len(lst1) <= len(lst2)

	idx = 0
	while idx < len(lst1):
		left = bisect_left(lst1, lst1[idx])
		right = bisect_right(lst1, lst1[idx])
		number_elem_lst1 = right - left
		
		left = bisect_left(lst2, lst1[idx])
		right = bisect_right(lst2, lst1[idx])
		number_elem_lst2 = right - left

		#Поиск минимального количества вхождений текущего элемента в оба списка
		min_num = min(number_elem_lst1, number_elem_lst2)
		
		# есть два списка. мы внутри списка на текщем элементе на уникальной
		# букве списка и мы знаем сколько таких элементов во втором списке
		# мин значение это сколько раз повторяется элемент.

		# Добавляем общий элемент (если он найден) в результирющий список нужное количество раз.
		# добавляем в конец списка новый список, сгенерированный
		# с помощью перегруженной для списков операции умножения из текущего элемента 
		# повторенного n-раз.

		# Создаем список из текущего элемента lst1
		# Дублируем его min_num раз (с помощью перегруженной операции умножения) 
		# Добавляем этот списое дубликатов в конец списка result
		result.extend([lst1[idx]] * min_num)

		assert number_elem_lst1 > 0
		idx = idx + number_elem_lst1

	assert len(result) <= len(lst1)

	return result

		# 1) найти кол-во элементов lst1[idx] в списке lst1
		# 2) найти количество элементов в lst1[idx] в списке lst2
		# добавить в результирующий список min[1), 2)] элементов lst1
		# сместить индекс на количество одинаковых элементов (длина диапазона эквивалентности текущего элемента) в левом списке.
	 	# вернуть результат


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
assert common_elements([2, 1], [1, 1, 2]) == [1, 2]
assert common_elements([1, 1, 1], [1]) == [1]
assert common_elements([1, 1, 1], [1, 1]) == [1, 1]
assert common_elements([1], [1, 1, 1]) == [1]
assert common_elements([1, 1], [1, 1, 1]) == [1, 1]
assert common_elements([1, 1, 2, 2, 2], [2, 2, 1, 1, 1]) == [1, 1, 2, 2]