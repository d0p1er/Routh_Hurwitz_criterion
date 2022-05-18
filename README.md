# Критерий Рауса-Гурвица

# Содержание
1. [Введение](#intro)

<a name="intro"></a>
## 1. Введение

Данная программа позволяет определить является ли система асимптотически устойчивой или нет, использую критерий Рауса-Гурвица.

## 2. Формулировка критерия

Для полинома <img src="https://latex.codecogs.com/png.image?%20%20p%20=%20a_0%20*%20x^n%20+%20a_1%20*%20x^{n-1}%20+%20...%20+%20a_n%20=%200"/> Матрица Рауса-Гурвица:
<img src="https://latex.codecogs.com/png.image?RH%20=%20%20\begin{pmatrix}%20%20%20a_{1}%20&%20a_{0}%20&%20\cdots%20&%200%20\\%20%20%20a_{3}%20&%20a_{2}%20&%20\cdots%20&%200%20\\%20%20%20\vdots%20%20&%20\vdots%20%20&%20\ddots%20&%20\vdots%20%20\\%20%20%200%20&%200%20&%20\cdots%20&%20a_{n}%20%20\end{pmatrix}"/>


Тогда, для того, чтобы система была асимптотически устойчива необходимо и достаточно, чтобы выполнялись соотношения


<img src="https://latex.codecogs.com/png.image?%20\Delta_1%20%3E%200,%20\Delta_2%20%3E%200%20...%20\Delta_n%20%3E%200"/>

То есть матрица Рауса-Гурвица должна быть положительно определенной.

## 3. Формат входных данных

На данный момент есть возможность определять асимптотическую устойчивость через матрицы **A**, **B**, **C**. Помимо int и float, на вход могут подаваться переменные
в формате латинской буквы, или же даже целые выражения.

## 4. Пример выполнения

```python
[out] Введите размерность матрицы:
[in]  2
[out] Будут ли переменные в матрицах A, B, C (y/n):
[in]  n
[out] Введите матрицы A, B, C в формате (в примере размерность матрицы 3x3):
[out] 1 2 3
[out] 4 5 6
[out] 7 8 9


[out] A:
[in]  1 0
[in]  0 1

[out] B:
[in]  1 0
[in]  0 1

[out] C:
[in]  1 -1
[in]  -1 1

[out] Система не является асимптотически устойчивой!
```

```python
[out] Введите размерность матрицы:
[in]  2
[out] Будут ли переменные в матрицах A, B, C (y/n):
[in]  y
[out] Введите матрицы A, B, C в формате (в примере размерность матрицы 3x3):
[out] 1 2 3
[out] 4 5 6
[out] 7 8 9


[out] A:
[in]  1 0
[in]  0 b

[out] B:
[in]  1 0
[in]  0 1

[out] C:
[in]  1 -a
[in]  -1 1

[out] Система асимптотически устойчива если:
[out] (-1 < b) & (b < oo)
[out] (-oo < b) & (b < oo)
[out] a*(b + 1)**2 > -b**2 - 3
```