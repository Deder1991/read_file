data = []
counte = 0
addnumber = 0
average = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		counte += 1
		addnumber = len(line) + addnumber
		if counte % 10000 == 0:  #印出目前進度
			print(counte)
average = addnumber / len(data)

print('總共有', len(data), '筆資料')
print('留言平均長度是', average)
