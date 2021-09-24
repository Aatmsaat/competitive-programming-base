def fastpow(num, pw):
	res = 1
	while pw:
		if pw&1: res *= num
		num *= num
		pw >>=1
	return res
