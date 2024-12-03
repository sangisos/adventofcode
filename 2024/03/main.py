import re

def main():
	lines = list()
	
	#with open("input_test.txt") as f:
	with open("input_test_2.txt") as f:
	#with open("input.txt") as f:
		for line in f:
			lines.append(line)
	if lines == None:
		return -1
	s=0
	s2=0
	line = ''.join(lines)
	r = re.findall(r'mul\([0-9]+,[0-9]+\)', line)
	#rem = ''.join(re.findall(r'(?:^|do\(\))(.*)(?:don\'t\(\)|$)', line))
	#r2 = re.findall(r'mul\([0-9]+,[0-9]+\)', rem)
	#mulordont = re.findall(r'(?:don\'t\(\).*?do\(\))|(mul\([0-9]+,[0-9]+\))', line)
	#print(mulordont)
	#r2 = list(filter(None, mulordont))
	donts = line.split('don\'t()')
	ccat=donts[0]
	for p in donts[1:]:
		ccat += p[p.find('do()'):]
	r2 = re.findall(r'mul\([0-9]+,[0-9]+\)', ccat)
	#print(donts)
	#r2 = re.findall(r'(?^|do\(\)).*mul\([0-9]+,[0-9]+\)', line)
	for m in r:
		mul=[int(n) for n in m.strip("mul(").strip(")").split(",")]
		s += mul[0]*mul[1]
	for m in r2:
		mul=[int(n) for n in m.strip("mul(").strip(")").split(",")]
		s2 += mul[0]*mul[1]

	print( r2, s, s2)

if __name__ == "__main__":
	main()

