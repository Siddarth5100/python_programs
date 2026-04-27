que = [2, 0, 4, 6, 0, 8, 9, 0, 0, 1]

# print(que)
# que.sort(reverse=True)
# print(que)
# que.sort()
# print(que)

# que = [2, 4, 6, 8, 9, 1]
# count_of_zero = 4
# que = [2, 4, 6, 8, 9, 1, 0, 0, 0, 0]

# que = [2, 0, 4, 6, 0, 8, 9, 0, 0, 1]

print(que)
count = 0
# for idx, num in enumerate(que):
    # print(num)
    # print(idx, num)
while 0 in que:
    count += 1
    que.remove(0)

print(count)

for num in range(count):
    # print(num)
    que.append(0)

        # que.pop(idx)
        # que.pop()
        # del que[idx]
        # que.clear()

print(que)


''' 
# [2, 4, 6, 8, 9, 1]
# zero = 4
# [2, 4, 6, 8, 9, 1, 0, 0, 0, 0]

# with 2 lists

count = 0
que_1 = []

for num in que:
    # print(num)
    if num == 0:
        count += 1
# print(count)
    else:
        que_1.append(num)
# print(que_1)

for no in range(count):
    que_1.append(0)
# print(que_1)
'''
