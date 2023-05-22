f = open('24_2.txt')
a = [x for x in f]
k = 0
for x in range(0, len(a)):
    if a[x].count('A') > a[x].count('E'):
        k += 1
print(k)
