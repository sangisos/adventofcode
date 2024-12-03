import re

def main():
	#with open("input_test.txt") as f:
	with open("input_test_2.txt") as f:
	#with open("input.txt") as f:
		line = ''.join([l.rstrip() for l in f])
	
	s1 = 0
	r1 = re.findall(r'mul\([0-9]+,[0-9]+\)', line)
	for m in r1:
		x, y = [int(n) for n in m.strip("mul(").strip(")").split(",")]
		s1 += x * y
	
	s2 = 0
	r2 = list(filter(None, re.findall(r'(?:don\'t\(\).*?do\(\))|(mul\([0-9]+,[0-9]+\))', line)))
	for m in r2:
		x, y = [int(n) for n in m.strip("mul(").strip(")").split(",")]
		s2 += x * y
	
	print("Part 1:", s1, "Part 2:", s2)

if __name__ == "__main__":
	main()
