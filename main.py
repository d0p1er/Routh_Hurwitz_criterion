import numpy as np
from sympy import *


VARS = False

def main():
	global VARS

	dimension = readDimension()
	VARS = readVars()

	print('Введите матрицы A, B, C в формате (в примере размерность матрицы 3x3):\n1 2 3\n4 5 6\n7 8 9\n')

	print('\nA:')
	A = readMatrix(dimension)
	print('\nB:')
	B = readMatrix(dimension)
	print('\nC:')
	C = readMatrix(dimension)
	print()

	lamba = symbols(u'λ')

	matrix_lamba = A*lamba**2 + B*lamba + C
	polynomial = Poly(matrix_lamba.det(), lamba)

	RH = getRHMatrix(polynomial)
	solution = criterionSylvester(RH)

	if (VARS):
		print('Система асимптотически устойчива если:')
		for sol in solution:
			print(sol)
	else:
		if (solution):
			print('Система асимптотически устойчива!')
		else:
			print('Система не является асимптотически устойчивой!')

	return 0


def readDimension():
	n_str = input('Введите размерность матрицы:\n')
	
	try:
		return int(n_str)
	except ValueError:
		print(n_str, 'must be INTEGER! Please, rewrite dimension...')
		
		return readDimension()


def readVars():
	const_in = input('Будут ли переменные в матрицах A, B, C (y/n):\n')
	
	if (const_in == 'y'):
		return True
	elif (const_in == 'n'):
		return False
	else:
		print(const_in, 'isn`t "y" or "n"')
		return readVars()


def readMatrix(n):	
	matrix = Matrix()

	i = 0
	while (i < n):
		row_str = input()

		try:
			row_str = row_str.split()
			if (len(row_str) != n):
				print('Row lenght ({}) isn`t equal dimension ({})! Please, rewrite row...'.format(len(row_str), n))
				
				continue
			tmp = []
			for r in row_str:
				tmp.append(parse_expr(r))

			matrix = matrix.row_insert(i, Matrix([tmp]))

			i += 1
		except ValueError as err:
			print(str(err).split()[-1], 'must be float or variables! Please, rewrite row...')

	return matrix


def getRHMatrix(polynomial):
	polynomial_coefs = polynomial.all_coeffs()
	dimension = degree(polynomial)
	
	RH = zeros(dimension, dimension)

	for i in range(dimension):
		for j in range(dimension):
			n_coef = 2 * j - i + 1

			if (0 <= n_coef and n_coef <= dimension):
				RH[i, j] = polynomial_coefs[n_coef]

	return RH


def criterionSylvester(matrix):	
	dimension = shape(matrix)[0]

	if (VARS):
		sys_inequalities = []

		for i in range(1, dimension + 1):
			d = matrix[:i, :i].det()
			variables = Poly(d).free_symbols

			for var in variables:
				try:
					sys_inequalities.append(factor(solve(d > 0, var)))
				except:
					pass

		return sys_inequalities
	else:
		for i in range(1, dimension + 1):
			if (matrix[:i, :i].det() <= 0):
				return False

		return True


if (__name__ == "__main__"):
	main()