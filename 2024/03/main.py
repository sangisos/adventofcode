import re

def main():
	lines = list()
	
	with open("input_test.txt") as f:
	#with open("input.txt") as f:
		for line in f:
			lines.append(line)
	if lines == None:
		return -1
	s=0
	for line in lines:
		r = re.findall(r'mul\([0-9]+,[0-9]+\)', line)
		for m in r:
			mul=[int(n) for n in m.strip("mul(").strip(")").split(",")]
			s += mul[0]*mul[1]
		

	print(lines, r, s)

if __name__ == "__main__":
	main()

