#to remove any element from the heap in O(1) time
from heapq import heappop, heappush

k = int(input('Enter the size of heap:- '))

#format to insert element input 1, element & to delete element input -1, element
#Note , The element to be deleted must be present in the heap
#It will give the result of sum of top k elements after all procedure of input and deletion
heap, heap_del, remaining, remaining_del = [], [], [], []
ans = curr = size = 0 #this must be taken into account if you want to delete element in O(1) time
for _ in range(int(input("Enter No. of Inputs:- "))):
    check, val = map(int, input().split())
    if check == 1:
        #Now removing impurities i.e. to check if any element to be deleted is in top
        while heap and heap_del and heap[0] == heap_del[0]: heappop(heap); heappop(heap_del)
        heappush(heap, val)
        curr += val
        size += 1
        if size > k:
            v = heappop(heap)
            heappush(remaining, -v)
            size -= 1
            curr -= v
        ans = max(ans, curr)
    else:
        #Now removing impurities i.e. to check if any element to be deleted is in top
        while remaining and remaining_del and remaining[0] == remaining_del[0]: heappop(remaining); heappop(remaining_del)
        if remaining and val<=-remaining[0]:
            heappush(remaining_del, -val)
            continue
        #In not in remaining then it must be in heap
        curr -= val
        size -= 1
        heappush(heap_del, val)
        if remaining:
            v = -heappop(remaining)
            curr += v
            size += 1
            heappush(heap, v)

print(ans)
            
