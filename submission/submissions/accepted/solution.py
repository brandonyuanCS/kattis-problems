import sys
import heapq

def solve():
    input_data = sys.stdin.read().split()
    
    n = int(input_data[0])
    k = int(input_data[1])
    limit = int(input_data[2])
    readings = [int(x) for x in input_data[3:3+n]]
    levels = [int(x) for x in input_data[3+n:3+n+k]]
    
    multipliers = [1] * (n + 1)
    i = 0
    currmult = 1
    for length in range(1, n + 1):
        while i < k and length > levels[i]:
            currmult += 1
            i += 1
        multipliers[length] = currmult

    maxlen = 0
    l = 0
    minheap = [] # (value, index)
    maxheap = [] # (-value, index) for max heap
    for r in range(n):
        val = readings[r]
        heapq.heappush(minheap, (val, r))
        heapq.heappush(maxheap, (-val, r))
        
        while l <= r:
            while minheap and minheap[0][1] < l:
                heapq.heappop(minheap)
            while maxheap and maxheap[0][1] < l:
                heapq.heappop(maxheap)
                
            currmin = minheap[0][0]
            currmax = -maxheap[0][0]
            len_currwindow = r - l + 1
            mult = multipliers[len_currwindow]
            
            if (currmax - currmin) * mult <= limit:
                break 
            else:
                l += 1 
        max_len = max(maxlen, r - l + 1)
    print(maxlen)

if __name__ == '__main__':
    solve()