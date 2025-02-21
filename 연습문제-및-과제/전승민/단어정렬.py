n = int(input())

temp = []

for i in range(0, n):
    a = input()
    temp.append(a)

temp = list(set(temp))
temp.sort()
temp.sort(key=len)

for i in temp:
    print(i)
