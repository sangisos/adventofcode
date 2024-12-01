

def main():
	lists = [[],[]]
	#with open("input_test") as f:
	with open("adventofcode.com_2024_day_1_input.txt") as f:
		for l in f.readlines():
			ids = l.split()
			for i in range(len(lists)):
				lists[i].append(int(ids[i]))
				
	
	for l in lists:
		l.sort()
	
	left_occurences = {}
	for n in lists[0]:
		if n in left_occurences:
			left_occurences[n] += 1
		else:
			left_occurences[n] = 1
		
	sim = 0
	for k,v in left_occurences.items():
		sim += k * v * lists[1].count(k)
		print(k,v,lists[1].count(k))
	tot = 0
	for i in range(len(lists[0])):
		tot += abs(lists[0][i]-lists[1][i])
	print(tot, sim)

	
if __name__ == "__main__":
	main()
