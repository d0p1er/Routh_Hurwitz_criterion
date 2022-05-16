import numpy as np
from sympy import symbols, Matrix, Poly
from sympy import *


def getDet(matrix):
	return np.linalg.det(matrix)

def readAll():
	n = readDimension()

	readMatrix(n)

def readDimension():
	n_str = input('Введите размерность матрицы:\n')
	
	try:
		return int(n_str)
	except ValueError:
		print(n_str, 'must be INTEGER! Please, rewrite dimension...')
		
		return readDimension()

def readMatrix(n):
	print('Введите матрицу в формате (в примере размерность матрицы 3x3):\n1 2 3\n4 5 6\n7 8 9\n\n')	
	matrix = np.empty((0, n), int)

	i = 0
	while (i < n):
		matrix_str = input()

		try:
			matrix_str = matrix_str.split()
			if (len(matrix_str) != n):
				print('Row lenght ({}) isn`t equal dimension ({})! Please, rewrite row...'.format(len(matrix_str), n))
				
				continue

			tmp = list(map(int, matrix_str))
			matrix = np.vstack([matrix, tmp])

			i += 1
		except ValueError as err:
			print(str(err).split()[-1], 'must be INTEGER! Please, rewrite row...')


	return matrix


# mat = np.array([[pol_1, pol_3], [pol_3, pol_2]])

a = symbols(u'α')
b = symbols(u'β')
l = symbols(u'λ')

A = Matrix([[1, 0], [0, b]])
B = Matrix([[1, 0], [0, 1]])
C = Matrix([[1, -a], [-1, 1]])

pol = A*(l**2) + B*l + C
pol = Poly(pol.det(), l).all_coeffs()
print(pol)

RH = zeros(4, 4)
print(RH)

for i in range(4):
	for j in range(4):
		n_coef = 2 * j - i + 1

		if (0 <= n_coef and n_coef <= 4):
			RH[i, j] = pol[n_coef]

pprint(RH)
# print(RH[:3, :3].det())
print()

print(factor(solve((RH[:1, :1].det() > 0, pol[0] > 0, pol[1] > 0, pol[2] > 0, pol[3] > 0, pol[4] > 0, RH[:3, :3].det() > 0), a)))
print(factor(solveset((RH[:1, :1].det() > 0) & (pol[0] > 0) & (pol[1] > 0) & (pol[2] > 0) & (pol[3] > 0) & (pol[4] > 0) & (RH[:3, :3].det() > 0))))
# M = Matrix(([x , y], [a, b]))
# print(M.det())

# print(mat)

# readAll()

# empty_array = np.array([])

# to_append = np.array([1, 2, 3])


# combined_array = np.append(empty_array, to_append)


# print(combined_array)