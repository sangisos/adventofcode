

def main():
	lines, rules = list(), dict()
	firsthalf = True
	with open("input_test_1.txt") as f:
	#with open("input.txt") as f:
		for line in f:
			if line == '\n':
				firsthalf = False
				continue
			if firsthalf:
				r, p = [int(n) for n in line.rstrip().split('|')]
				if r in rules:
					rules[r].append(p)
				else:
					rules[r] = [p]
			else:
				lines.append([int(n) for n in line.rstrip().split(',')])
	
	#print(rules, lines)
	
	sum1 = 0
	for update in lines:
		valid = True
		for idx, page in enumerate(update):
			#print(update[:idx])
			if page in rules and any([i in update[:idx] for i in rules[page]]):
				#print("update:", update, "rule broken:", page, "|", rules[page])
				valid = False
				break
		if valid:
			#print("update:", update[:len(update)//2], update[len(update)//2], update[len(update)//2+1:])
			sum1 += update[len(update)//2]
	
	sum2 = 0
	
	print("Part 1:", sum1, "Part 2:", sum2)

if __name__ == "__main__":
	main()
