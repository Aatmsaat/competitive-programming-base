#Author :- Aatmsaat
#Email :- vaibhav61199@gmail.com

import time

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
	
	wrds = ['apple', 'banana', 'guava', 'pomogranate', 'orange', 'grapes', 'mango']*int(1e3)
	print('ok')
	search = ['apple', 'banana', 'hell', 'biradar','callone', 'don', 'mango', 'man', 'ora', 'pomogranate', 'watermellon', 'guav', 'doll']
	
	t = trie()
	for w in wrds:
		t.add(w)
	start = time.time()
	for _ in range(int(1e2)):
		for s in search:
			t.find(s)
		#print(s, t.find(s))
	print(time.time()-start, '\n')#0.015203237533569336
	
	start = time.time()
	for _ in range(int(1e2)):
		for s in search:
			f = False
			for w in wrds:
				if w==s:
					f = True
					break
		#print(s, f)
	print(time.time()-start)#3.963283061981201
	
	'''
	Conclusion when large no. of words the use 'trie data-structure'
	Otherwise use 'Nomal Search :)'
	'''
