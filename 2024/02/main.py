from itertools import pairwise


def main():
	reports = []
	#with open("input_test") as f:
	with open("input.txt") as f:
		for line in f:
			reports.append([int(n) for n in line.split()])
	safe = [0, 0]
	for report in reports:
		pw = list(pairwise(report))
		f = [lambda ab: ab[0]<ab[1]<=ab[0]+3, lambda ab: ab[0]-3<=ab[1]<ab[0]]
		ltgt = [f[0](x) for x in pairwise(report)], [a-3<=b<a for (a,b) in pairwise(report)]
		#print([f[1](ab) for ab in pairwise(report)])
		#print(list(map(f[0], pw)))
		# First half
		#print(any(map(all, ltgt)))
		if any(map(all, ltgt)):
			for i in [0,1]:
				safe[i]+=1
			continue
		
		# Second half
		for i in [0,1]:
			if ltgt[i].count(False) <= 2:
				print(["rising","falling"][i], ltgt[i].count(False))
				print(pw)
				print(report)
				rem = [report[:ltgt[i].index(False)]+report[ltgt[i].index(False)+1:],
				       report[:ltgt[i].index(False)+1]+report[ltgt[i].index(False)+2:]]
				print(rem)
				remp = [pairwise(rem[0]), pairwise(rem[1])]
				rembool = ([[f[i](x) for x in l] for l in remp])
				if any(map(all, rembool)):
					safe[1] += 1
				
	print(safe)

if __name__ == "__main__":
	main()
