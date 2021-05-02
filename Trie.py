class tnode:
	def __init__(self):
		self.arr = [None]*26
		self.wend = 0
		
class trie:
	
	def __init__(self):
		self.root = tnode()
		
	def add(self, wrd):
		curr = self.root
		for c in wrd:
			idx = ord(c)-ord('a')
			if curr.arr[idx]:
				curr = curr.arr[idx]
				continue
			new = tnode()
			curr.arr[idx] = new
			curr = new
		curr.wend += 1
		
	def find(self, wrd):
		curr = self.root
		for c in wrd:
			idx = ord(c)-ord('a')
			if not curr.arr[idx]:
				return False
			curr = curr.arr[idx]
		return True if curr.wend else False
		
if __name__ == '__main__':
	n = int(input('Enter no. of words: '))
	t = trie()
	for _ in range(n):
		t.add(input().strip())
		
	print('Enter values to search\nYou can end searh by input 0')
	while True:
		word = input().strip()
		print(t.find(word))
