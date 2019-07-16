# 讀取 reviews.txt 檔

data = []
with open('reviews.txt', 'r') as file:
    for message in file:
        data.append(message)  # append 新增 message 至 data 清單裡
#       print(len(data))    # 會一筆一筆列出
print(len(data))    # len 字串的長度  總直接列出筆數
# print(data[2])
# print('-----------------------------')
# print(data[4])

sum_len = 0
for m in data:
	sum_len = sum_len + len(m)
print('留言的平均長度為', sum_len/len(data))