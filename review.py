# 讀取 reviews.txt 檔

data = []
with open('reviews.txt', 'r') as file:
    for message in file:
        data.append(message)  # append 新增 message 至 data 清單裡
print(len(data))    # len 字串的長度
print(data[2])
print('-----------------------------')
print(data[4])