import numbers

TESTING = True

def ew_add(vector1, *vector2):
	#print("vector1",vector1)
	#print("vector2",vector2)
	#print("vector2[0]",vector2[0])
	#print("*vector2",*vector2)
	#print("type(vector1) is not list", type(vector1) is not list)
	#print("type(vector2) is not list", type(vector2) is not list)
	#print("type(*vector2) is not list", type(*vector2) is not list)
	#print("type(vector2[0]) is not list", type(vector2[0]) is not list)
	#print("type(vector2[0])",type(vector2[0]))
	if len(vector2)==1:
		v2 = vector2[0]
	else:
		v2 = [*vector2]
	if isinstance(vector1, numbers.Number):
		if isinstance(v2, numbers.Number):
			return vector1 + v2
		return [vector1 + x for x in v2]
	else:
		if isinstance(v2, numbers.Number):
			return [x + v2 for x in vector1]
		if len(vector1) == len(v2):
			return [x + y for (x, y) in zip(vector1, v2)]
	raise ValueError("Invalid Arguments.")

assert(ew_add(1, 2) == 3)
assert(ew_add(1, [2, 3]) == [3, 4])
assert(ew_add(1, 2, 3) == [3, 4])
assert(ew_add([1, 2], 3) == [4, 5])
assert(ew_add([1, 2], [3, 4]) == [4, 6])
assert(ew_add([1, 2], 3, 4) == [4, 6])

def v_add(vector1, *vector2):
	if len(vector2)==1:
		v2 = vector2[0]
	else:
		v2 = [*vector2]


def ew_mul(vector1, *vector2):
	if len(vector2)==1:
		v2 = vector2[0]
	else:
		v2 = [*vector2]
	if isinstance(vector1, numbers.Number):
		if isinstance(v2, numbers.Number):
			return vector1 * v2
		return [vector1 * x for x in v2]
	else:
		if isinstance(v2, numbers.Number):
			return [x * v2 for x in vector1]
		if len(vector1) == len(v2):
			return [x * y for (x, y) in zip(vector1, v2)]
	raise ValueError("Invalid Arguments.")

assert(ew_mul(2, 3) == 6)
assert(ew_mul(3, [1, 2]) == [3, 6])
assert(ew_mul(3, 2, 1) == [6, 3])
assert(ew_mul([1, 2], 3) == [3, 6])
assert(ew_mul([1, 2], [3, 4]) == [3, 8])
assert(ew_mul([1, 2], 3, 4) == [3, 8])


def get_directions(letter_coords, lineno, charno):
	directions = []
	for i in [-1,0,1]:
		for j in [-1,0,1]:
			if [lineno+i, charno+j] in letter_coords:
				directions.append([i, j])
	return directions

def get_directions_diag(letter_coords, lineno, charno):
	directions = []
	for i in [-1,1]:
		for j in [-1,1]:
			if [lineno+i, charno+j] in letter_coords:
				directions.append([i, j])
	return directions

def main():
	lines = list()
	
	with open(("input_test_1.txt" if TESTING else "input.txt")) as f:
		print(f.name)
		for line in f:
			lines.append(line.rstrip())
	
	Xs, Ms, As, Ss = [], [], [], []
	for idline, line in enumerate(lines):
		for idc, c in enumerate(line):
			if c == 'X':
				Xs.append([idline, idc])
			if c == 'M':
				Ms.append([idline, idc])
			if c == 'A':
				As.append([idline, idc])
			if c == 'S':
				Ss.append([idline, idc])
	
	sum1 = 0
	
	for x in Xs:
		dirm = get_directions(Ms, *x)
		for d in dirm:
			if ew_add(x, ew_mul(2,d)) in As and ew_add(x, ew_mul(3,d)) in Ss:
				sum1 += 1
		
	sum2 = 0
	
	for a in As:
		dir_m = get_directions_diag(Ms, *a)
		if len(dir_m) == 2:
			if all([ew_add(a, ew_mul(-1, d)) in Ss for d in dir_m]):
				sum2 += 1
	
	print("Part 1:", sum1, "Part 2:", sum2)
	
	if TESTING: assert(sum1 == 18)
	if TESTING: assert(sum2 == 9)
	

if __name__ == "__main__":
	main()
