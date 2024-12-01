

def main():
	lists = [[],[]]
	#with open("input_test") as f:
	with open("adventofcode.com_2024_day_1_input.txt") as f:
		for l in f.readlines():
			ids = l.split()
			for i in range(len(lists)):
				lists[i].append(int(ids[i]))
				
	

	
	sim = 0
	for n in lists[0]:
		sim += n * lists[1].count(n)
	
	for l in lists:
		l.sort()
	tot = 0
	for i in range(len(lists[0])):
		tot += abs(lists[0][i]-lists[1][i])
	
	print(tot, sim)

	
if __name__ == "__main__":
	main()
