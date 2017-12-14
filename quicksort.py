num = [5, 8, 6, 2, 1, 9, 7, 4, 3]
numList = [[0, len(num) - 1]]	#分けたリストの位置のスタック

def left(pivot, lpos, maxN):
	for i in range(lpos, maxN + 1):
		if num[i] >= pivot:
			return i

	return -1

def right(pivot, minN, rpos):
	for i in range(minN, rpos + 1)[::-1]:
		if num[i] <= pivot:
			return i

	return -1
def change():
	global num, numList
	rang = numList[-1]
	lpos = rang[0]
	rpos = rang[1]
	ppos = int((rang[0] + rang[1]) / 2)
	pivot = num[ppos]
	if(rang[0] == ppos and rang[0] < rang[1]):
		numList.pop()
		return
	while 1:
		lpos = left(pivot, lpos, rang[1])
		rpos = right(pivot, rang[0], rpos)
		if lpos < rpos:
			num[lpos], num[rpos] = num[rpos], num[lpos]
			print(num)
			lpos += 1
			rpos -= 1
		else:
			numList.pop()
			if(rang[1] - lpos > 0):
				numList.append([lpos, rang[1]])
			if((lpos - 1) - rang[0] > 0):
				numList.append([rang[0], lpos - 1])

			break


while len(numList) != 0:
	change()
	#print(num)

print(num)
