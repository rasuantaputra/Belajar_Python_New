# tipe data: Angka satuan (integer)
data_integer = 1
print('data : ', data_integer)
print('- bertipe : ', type(data_integer))

# tipe data: Angka desimal (float)
data_float = 1.5
print('data : ', data_float)
print('- bertipe : ', type(data_float))

# tipe data: Karakter (string)
data_string = "python"
print('data : ', data_string)
print('- bertipe : ', type(data_string))

# tipe data: Boolean (boolean)
data_boolean1 = True
data_boolean2 = False
print('data : ', data_boolean1)
print('- bertipe : ', type(data_boolean1))

# # tipe data khusus

# bilangan kompleks
data_complex = complex(5,6)
print('data : ', data_complex)
print('- bertipe : ', type(data_complex))

# tipe data bahasa C
from ctypes import c_double, c_char

data_c_double = c_double(19.3)
print('data : ', data_c_double)
print('- bertipe : ', type(data_c_double))