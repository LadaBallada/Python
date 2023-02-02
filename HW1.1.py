i = input('Введите трёхзначное число')
i = int(i)

a = i // 100
b = i // 10 % 10
c = i % 100 % 10

print (a+b+c)