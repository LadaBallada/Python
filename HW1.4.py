n = input('высота шоколадки в дольках')
n = int(n)

m = input('ширина шоколадки в дольках')
m = int(m)

k = input('Сколько долек нужно отломить?')
k = int(k)

if k % m or k % n <0:
    print('no')

else:
    print('yes')