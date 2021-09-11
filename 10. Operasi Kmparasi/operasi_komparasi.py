"""
Sama dengan dunia nyata operasi komparasi di python

1. lebih dari (>)
2. kurang dari (<)
3. sama dengan (==)
4. lebih dari sama dengan (>=)
5. kurang dari sama dengan (<=)
7. tidak sama dengan (!=)

komparasi di sana untuk literal
"""

"""
yang akan dipelajari di sini adalah komparasi untuk assigment object
(is dan is not)

python 3 kebawah bisa menggunakan "is" dan "is not" untuk literal.
Tapi di python 3 udah gabisa

biasanya nanti akan digunakan saat menggunakan OOP
"""

x = 5
y = 5

# jika nanti di run, x dan y akan diletakan pada memory yang sama
# hal tersebut dikarenakan nilai x dan y sama (dari tipe data maupun nilai)
print('nilai x = ', x, ',id = ', hex(id(x)))
print('nilai y = ', y, ',id = ', hex(id(y)))

hasil =  x is y
# hasil =  x is not y

print('x is y = ', hasil) 



















