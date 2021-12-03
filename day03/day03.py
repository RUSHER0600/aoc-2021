import timeit

def main():
	# load data
	inp = []
	for line in open("input.dat"):
		inp.append(line.strip("\n"))
	
	# find power consumption
	gamma = ""
	epsilon = ""
	count = {
		"0": 0,
		"1": 0
	}

	for i in range(len(inp[0])):
		for line in inp:
			count[line[i]] += 1

		gamma += "0" if count["0"] > count["1"] else "1"
		epsilon += "0" if count["0"] < count["1"] else "1"

		count["0"] = 0
		count["1"] = 0

	print("Power Consumption: "+str(int(gamma, 2) * int(epsilon, 2)))

	# find life support rating
	newNums = {
		"0": [],
		"1": []
	}

	# oxgen generator bit criteria
	oxNums = inp
	for i in range(len(oxNums[0])):
		for n in oxNums:
			newNums[n[i]].append(n)

		if len(newNums["1"]) >= len(newNums["0"]):
			oxNums = newNums["1"].copy()
		else:
			oxNums = newNums["0"].copy()

		newNums["0"].clear()
		newNums["1"].clear()

		if len(oxNums) == 1:
			break

	# CO2 scrubber bit criteria
	co2Nums = inp
	for i in range(len(co2Nums[0])):
		for n in co2Nums:
			newNums[n[i]].append(n)

		if len(newNums["0"]) <= len(newNums["1"]):
			co2Nums = newNums["0"].copy()
		else:
			co2Nums = newNums["1"].copy()

		newNums["0"].clear()
		newNums["1"].clear()

		if len(co2Nums) == 1:
			break

	print("LS rating: "+str(int(oxNums[0], 2) * int(co2Nums[0], 2)))

print(timeit.timeit('main()', globals=locals(), number=1))