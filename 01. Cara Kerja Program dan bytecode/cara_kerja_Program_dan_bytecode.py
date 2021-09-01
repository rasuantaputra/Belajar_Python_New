import time

startTime = time.time()

print('halo')

"""
command untuk mengubah ke bytecode
windows :
python -m py_compile (nama file).py

linux/mac :
python -m py_compile (nama file).py
"""

# Menghitung kecepatan exsekusi bytecode dg interpreter
print(time.time() - startTime, 'detik')