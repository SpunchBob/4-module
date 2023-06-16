# maxi = 0
# num = 0
# n = int(input()) 
# for i in range(n):
#     a = int(input())
#     if a > maxi: maxi = a
#     if a == 0: num = 1
# print(maxi)
# if num > 0:
#     print('YES')
# else:
#     print('NO')

# max = 0
# porog = 80
# n = int(input())
# minimal = []
# for i in range(n):
#     a = int(input())
#     minimal.append(a)
# if a > 80:
#     print("YES")
# else:
#     print("NO")

# print(min(minimal))

kol = 0

for i in range(8):
    a = int(input())
    if a // 3 and a % 4:
        kol += 1
print(kol)