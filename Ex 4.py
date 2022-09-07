my_str = input('Введите слова через пробел')

my_str2 = my_str.split(' ')
print(my_str2)

z = 0
for word in my_str2:
    z = z + 1
    print(str(z), word[0:9])
