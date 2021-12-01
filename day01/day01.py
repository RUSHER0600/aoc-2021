import timeit

def main():
	# get sonar input
	inp = []
	for line in open("input.dat"):
		inp.append(int(line.strip("\n")))

	# number of increased measurements
	count = 0

	i = 1
	prevsum = 0
	while i < len(inp)-1:
		sum = inp[i-1] + inp[i] + inp[i+1]
		if sum > prevsum:
			count += 1
		prevsum = sum
		i += 1

	return count-1

#print(timeit.timeit('main()', number=5))
print(main())