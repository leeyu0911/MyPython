def c(a, b):
	if b == 0 or a == b:
		return 1
	return c(a-1, b) + c(a-1, b-1)
