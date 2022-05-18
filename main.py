import numpy as np
from sympy import *

# only using A B C
# all values are float
def readAll():
	n = readDimension()

	print('Введите матрицы A, B, C в формате (в примере размерность матрицы 3x3):\n1 2 3\n4 5 6\n7 8 9\n')

	print('\nA:')
	A = readMatrix(n)
	print('\nB:')
	B = readMatrix(n)
	print('\nC:')
	C = readMatrix(n)
	print()

	lamba = symbols(u'λ')

	matrix_lamba = A*lamba**2 + B*lamba + C
	polynomial = Poly(matrix_lamba.det(), lamba)
	RH = getRHMatrix(polynomial)
	print(criterionSylvester(RH))


def readDimension():
	n_str = input('Введите размерность матрицы:\n')
	
	try:
		return int(n_str)
	except ValueError:
		print(n_str, 'must be INTEGER! Please, rewrite dimension...')
		
		return readDimension()


def readMatrix(n):	
	matrix = Matrix()

	i = 0
	while (i < n):
		matrix_str = input()

		try:
			matrix_str = matrix_str.split()
			if (len(matrix_str) != n):
				print('Row lenght ({}) isn`t equal dimension ({})! Please, rewrite row...'.format(len(matrix_str), n))
				
				continue

			tmp = list(map(int, matrix_str))
			matrix = matrix.row_insert(i, Matrix([tmp]))

			i += 1
		except ValueError as err:
			print(str(err).split()[-1], 'must be INTEGER! Please, rewrite row...')


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

	for i in range(dimension):
		if (matrix[:i, :i].det() <= 0):
			return False

	return True


if (__name__ == "__main__"):
	readAll()