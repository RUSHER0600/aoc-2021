import timeit

def main():
	# submarine coordinates
	d = 0 # depth
	f = 0 # horizontal position
	a = 0 # aim

	for line in open("input.dat"):
		cmd, val = line.split(" ")
		val = int(val.strip("\n"))

		if cmd == "forward":
			f += val
			d += (a * val)
		elif cmd == "down":
			a += val
		elif cmd == "up":
			a -= val

	print(d * f)

print(timeit.timeit('main()', globals=locals(), number=1))