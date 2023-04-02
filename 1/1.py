'''
(x ∧ ¬y) ∨ (y ≡ z) ∨ ¬w
Фрагмент таблицы... при которых функция F ложна.
Определите, какому столбцу таблицы соответствует
каждая из переменных w, x, y, z.

Перем.1 Перем.2 Перем.3 Перем.4
???     ???     ???     ???
*       0       *       *
1       0       *       0
1       *       0       0
'''

print('x y z w')
for x in range(2):
    for y in range(2):
        for z in range(2):
            for w in range(2):
                if not((x and not y) or (y == z) or not w):
                    print(x, y, z, w)
                          
'''
x y z w
0 0 1 1
0 1 0 1
1 1 0 1
'''
