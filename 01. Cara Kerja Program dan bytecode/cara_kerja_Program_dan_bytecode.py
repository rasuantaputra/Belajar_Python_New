import time

startTime = time.time()

print('halo')

print('1')
print('2')
print('3')
print('4')
print('5')
print('6')
print('7')
print('8')
print('9')

"""
command untuk mengubah ke bytecode
windows :
python -m py_compile (nama file).py

linux/mac :
python -m py_compile (nama file).py
"""

# Menghitung kecepatan exsekusi bytecode dg interpreter
print(time.time() - startTime, 'detik')