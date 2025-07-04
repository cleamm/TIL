# lst = [[2, 16, 21, 6, 1],
#  [14, 8, 15, 17, 3],
#  [25, 9, 12, 20, 23],
#  [7, 18, 11, 13, 24],
#  [22, 5, 19, 10, 4]]
import random
nums = list(range(1,26))
random.shuffle(nums)
lst = []
for i in range(5):
    lst2 = []
    for j in range(5):
        num = random.choice(nums)
        lst2.append(num)
        nums.remove(num)
    lst.append(lst2)

    
all_lst = []
low_num = 0
for i in lst:
    all_lst += i
all_lst.sort()

res = [list(0 for i in range(5)) for i in range(5)]
 
min_col = min_row = 0
max_col = max_row = 4
while(len(all_lst) != 0):
    for i in range(min_row, max_row+1): # 오른쪽입력
        if(res[min_row][i] == 0):
            res[min_row][i] = all_lst[0]
            del all_lst[0]

    for i in range(min_col, max_col+1): # 아래 입력
        if(res[i][max_col] == 0):
            res[i][max_col] = all_lst[0]
            del all_lst[0]

    for i in range(max_row, min_row-1, -1): # 왼쪽입력
        if(res[max_col][i] == 0):
            res[max_col][i] = all_lst[0]
            del all_lst[0]

    max_col -= 1
    for i in range(max_col, min_col, -1): # 위 입력
        if(res[i][min_row] == 0):
            res[i][min_row] = all_lst[0]
            del all_lst[0]
    min_row += 1 

print('result')
for i in res:
    print(i)