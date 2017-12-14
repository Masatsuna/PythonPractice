#スタック使う？
num = [5, 8, 6, 2, 1, 9, 7, 4, 3]
numlist = list()
p = int(len(num) / 2)
x = 0
y = len(num)

def left(min):
	for i in range(min, len(num)):
		if num[i] >= num[p]:
			return i
			break
			
def right(max):
	for i in range(0, max)[::-1]:
		if num[i] <= num[p]:
			return i
			break

def change(n):			
	while():			
		lnum = left(x)
		rnum = right(y)
		if lnum < rnum:
			n[x], n[y] = n[y], n[x]
		else if lnum > rnum:
			
		else if lnum == rnum:
			
	
	numlist.append(n[0:x-1])
	numlist.append(n[x: len(num)])

change(num)
