# casting adalah merubag jenis tipe data
# misal kaya dari int ke float atau sebliknya

data = 9.3

print('data = ',  data, 'type : ', type(data))

data_int = int(data)
data_float = float(data)
data_str = str(data)
data_bool = bool(data) # akan False jika data bernilai 0

print('data = ', data_int, 'tipe : ', type(data_int))
print('data = ', data_float, 'tipe : ', type(data_float))
print('data = ', data_str, 'tipe : ', type(data_str))
print('data = ', data_bool, 'tipe : ', type(data_bool))