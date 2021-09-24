def fastexpo(num, pw):
	if pw == 1: return num
	res = num if pw&1 else 1
	return res*(fastexpo(num, pw>>1)**2)
