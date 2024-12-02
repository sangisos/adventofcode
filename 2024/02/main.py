from itertools import pairwise


def main():
	reports = []
	with open("input.txt") as f:
		for line in f:
			reports.append([int(n) for n in line.split()])
	safe = 0
	for report in reports:
		pw = []
		pw.extend(pairwise(report))
		if all([a<b<=a+3 for (a,b) in pw]) or all([a-3<=b<a for (a,b) in pw]):
			safe += 1
	print(safe)

if __name__ == "__main__":
	main()
