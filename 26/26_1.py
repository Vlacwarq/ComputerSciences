f = open('27882.txt')
S = 1405
K = 5560
a = [int(x) for x in f]
a_sorted = sorted(a)
summa = 0
count = 0
arr = []

for i in range(0, len(a_sorted)):
    if summa < S:
        count += 1
        summa += a_sorted[i]
        arr.append(a_sorted[i])
    else:
        break
    print(count, summa, max(arr))

# Answer 369 | 9
