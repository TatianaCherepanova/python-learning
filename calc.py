import math

#TODO функция, которая принимает числа и выполнят операции над ними
def calc(a, b, operator):
	
	if operator == " - ":
		return a - b
	elif operator == " + ":
		return a + b
	elif operator == " * ":
		return a * b
	elif operator == " / ":
		if b == 0:
			return "forbidden operand"
		return a / b
	else:
		return "unknown operator"



def calc_n_print(a, b, op):
	rslt = calc(a, b, op)
	print(str(a) + op + str(b) + " = " + str(rslt))
	return rslt


assert 5 == calc_n_print(7, 2, " - ")
assert 39 == calc_n_print(36, 3, " + ")
assert 8 == calc_n_print(2, 4, " * ")
assert 4 == calc_n_print(28, 7, " / ")
assert math.isclose(5.3, calc_n_print(2.2, 3.1, " + "))
assert math.isclose(0.3, calc_n_print(4.3, 4, " - "))
assert "unknown operator" == calc_n_print(1, 1, " ")
assert -12 == calc_n_print(-9, -3, " + ")
assert -3 == calc_n_print(-1, 3, " * ")
assert 0 == calc_n_print(-10, 10, " + ")
assert "forbidden operand" == calc_n_print(3, 0, " / ")
assert math.isclose(-19.2, calc_n_print(6, -3.2, " * "))
