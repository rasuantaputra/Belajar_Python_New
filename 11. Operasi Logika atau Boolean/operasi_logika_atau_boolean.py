# operasi logika (seperti biasa sama dengan dunia nyata~)

# not (negasi), or (tambah), and (kali), xor (exlusive or)

# NOT
a = False
c = not a

print('data a =', a)
print('==========NOT==========')
print('data c =', c)

# OR
print('==========OR==========')
a = True
b = True
c = a or b
print(a, 'or', b, '=', c)

a = True
b = False
c = a or b
print(a, 'or', b, '=', c)

a = False
b = True
c = a or b
print(a, 'or', b, '=', c)

a = False
b = False
c = a or b
print(a, 'or', b, '=', c)

# AND
print('==========AND==========')
a = True
b = True
c = a and b
print(a, 'and', b, '=', c)

a = True
b = False
c = a and b
print(a, 'and', b, '=', c)

a = False
b = True
c = a and b
print(a, 'and', b, '=', c)

a = False
b = False
c = a and b
print(a, 'and', b, '=', c)

# XOR
print('==========XOR==========')
a = True
b = True
c = a ^ b
print(a, 'xor', b, '=', c)

a = True
b = False
c = a ^ b
print(a, 'xor', b, '=', c)

a = False
b = True
c = a ^ b
print(a, 'xor', b, '=', c)

a = False
b = False
c = a ^ b
print(a, 'xor', b, '=', c)