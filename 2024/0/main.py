

def main():
	lines = list()
	
	with open("input_test_1.txt") as f:
	#with open("input.txt") as f:
		for line in f:
			print(line.split())
			lines.append([int(n) for n in line.rstrip().split()])
	
	print(lines)

	sum1 = sum(lines[0])
	sum2 = sum(lines[1])
	
	print("Part 1:", sum1, "Part 2:", sum2)

if __name__ == "__main__":
	main()
