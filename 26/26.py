f = open('26_1.txt')
n = 5000
k = 0
a = [int(x) for x in f]
arr = []
for i in range(0,len(a)-1):
    for cc in range(0,len(a)-1):
        if (a[i] % 2 != 0 and a[i+1] % 2 == 0) or (a[i] % 2 == 0 and a[i+1] % 2 != 0) and (a[i+1]+a[i] == a[cc]):
            k+=1
            arr.append(a[i] + a[i+1])

print(max(arr),k)
