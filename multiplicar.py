def multiplica_r(m, d):
    print(m * d)


c = (input("numbers to multiplicate separated by x without spaces: "))

position = c.find("x")
m = c[0: position]
d = c[position + 1: 20]
j = int(m)
k = int(d)
print(multiplica_r(+j, +k))
