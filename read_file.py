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

filter_list = []
for filter_line in data:
	if len(filter_line) < 100:
	filter_list.append(filter_line)

print('總共有', len(filter_list),'筆資料長度小於100') 
