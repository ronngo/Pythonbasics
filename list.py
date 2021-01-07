import random


print('-----------------------')
print('Tạo 1 số nguyên ngẫu nhiên n trong khoảng [50, 1000]')
danh_sach = []
for n in range(1):
    danh_sach.append(random.randrange(50, 1000))
    print('%d' % danh_sach[n], end='')

print('')
print('')
print('-----------------------')
print('Sinh ngẫu nhiên 1 List các số nguyên trong khoảng [-1000, 1000]')
danh_sach = []
for n in range(10):
    danh_sach.append(random.randrange(-1000, 1000))
    print('%d,' % danh_sach[n], end='')


print('')
print('')
print('-----------------------')
print('Sinh ngẫu nhiên 1 List các số nguyên trong khoảng [-1000.0, 1000.0]')
danh_sach = []
for n in range(10):
    danh_sach.sam(random.randrange(-1000.0, 1000.0))
    print('%d,' % danh_sach[n], end='')






