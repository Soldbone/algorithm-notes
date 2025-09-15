# 설탕 배달

# [16] → 5*2 + 3*2
# [11] → 3: 5*1 + 3*2

N = int(input())

result = -1
num_of_5kg = N//5
for i in range(num_of_5kg, -1, -1):
    remain = (N - 5 * i)
    if ( remain % 3 == 0 ):
        result = i + remain // 3
        break
print(result)

#############################

# tjdrufeorhdzja님 코드
x = int(input())
a = 0
while x >= 0:
    if x % 5 == 0:
        a += (x//5)
        print(a)
        break
    x = x - 3
    a = a + 1
else:
    print(-1)