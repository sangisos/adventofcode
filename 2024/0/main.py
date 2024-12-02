

def main():
	lines = list()
	
	with open("input_test.txt") as f:
	#with open("input.txt") as f:
		for line in f:
			lines.append([int(n) for n in line.split()])
	if lines == None:
		return -1
	
	print(lines)

if __name__ == "__main__":
	main()

