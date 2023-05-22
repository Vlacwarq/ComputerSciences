f = open('zadanie24_2.txt')
s = f.readline()
max_k = 0;k = 0
for i in s:
    if (i == 'L' and k%3 == 0) or (i == 'D' and k%3 == 1) or (i == 'R' and k%3 == 2):
        k+=1
        if k > max_k:
            max_k = k
    elif i == 'L':
        k=1
    else:
        k = 0

print(max_k)

        

