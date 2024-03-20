n = int(input())
m = []
for i in range(n):
    m.append(input().split(" "))
print(m)
d = {}
c = 0
for i in range(len(m)):
    if int(m[i][0]) not in d:
        d[int(m[i][0])] = [c, int(m[i][2])]
        c += 1
    else:
        d[int(m[i][0])][1] += int(m[i][2])

answer = []
for i in d:
    answer.append([i, d[i][1]])
print(*answer)