import random

print("chuong trình tìm số lớn nhất trong danh sách !")
#[123, 3, 4, 3424, 4, 23, 423, 4, 23, 4]
# muon co so ngau nhien

danh_sach = []
for n in range(10):
    danh_sach.append(random.randrange(1, 1000))
    print('%d,' % danh_sach[n], end='')

vi_tri = 0
lasgest_number = danh_sach[vi_tri]
for n in range(len(danh_sach)):
    if danh_sach[n] > lasgest_number:
        lasgest_number = danh_sach[n]
        vi_tri = n
print('')
print('')
print('so lon nhat là: %d ' % lasgest_number)
print('tai vi tri: %d ' % vi_tri)
