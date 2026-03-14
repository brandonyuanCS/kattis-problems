import os
import random
import heapq

# --- 1. THE GROUND TRUTH SOLVER ---
# This guarantees your .ans files match your exact optimal logic
def get_answer(n, k, limit, readings, levels):
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
    minheap = []
    maxheap = []
    
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
                
        maxlen = max(maxlen, r - l + 1)
    return maxlen

# --- 2. FILE WRITING HELPER ---
def write_test_case(idx, n, k, limit, readings, levels):
    # Ensure directory exists
    os.makedirs('submission/data/secret', exist_ok=True)
    
    in_filename = f"submission/data/secret/secret{idx:02d}.in"
    ans_filename = f"submission/data/secret/secret{idx:02d}.ans"
    
    # Write .in file
    with open(in_filename, 'w') as f:
        f.write(f"{n} {k}\n")
        f.write(f"{limit}\n")
        f.write(" ".join(map(str, readings)) + "\n")
        f.write(" ".join(map(str, levels)) + "\n")
        
    # Generate and write .ans file
    ans = get_answer(n, k, limit, readings, levels)
    with open(ans_filename, 'w') as f:
        f.write(f"{ans}\n")
        
    print(f"Generated {in_filename} and {ans_filename} (Answer: {ans})")

# --- 3. TEST CASE GENERATORS ---
def generate_all_cases():
    idx = 1
    
    # Cases 1-6: General Random Cases (Varying sizes)
    for _ in range(6):
        n = random.randint(50, 5000)
        k = random.randint(5, min(n - 1, 100))
        limit = random.randint(100, 100000)
        readings = [random.randint(1, 100000) for _ in range(n)]
        levels = sorted(random.sample(range(1, n), k))
        write_test_case(idx, n, k, limit, readings, levels)
        idx += 1
        
    # Case 7: Edge - Minimum Bounds (n=1)
    write_test_case(idx, 1, 1, 10, [42], [1])
    idx += 1
    
    # Case 8: Edge - All Same
    n_same = 1000
    write_test_case(idx, n_same, 5, 50, [5] * n_same, [100, 200, 300, 400, 500])
    idx += 1
    
    # Case 9: Edge - Shattered Glass (Alternating extremes)
    n_shatter = 1000
    readings_shatter = [10 if i % 2 == 0 else 1000000 for i in range(n_shatter)]
    levels_shatter = sorted(random.sample(range(1, n_shatter), 10))
    write_test_case(idx, n_shatter, 10, 5, readings_shatter, levels_shatter)
    idx += 1
    
    # Case 10: Edge - Multiplier Trap (Flat readings, aggressive thresholds)
    n_trap = 2000
    readings_trap = [i // 100 for i in range(n_trap)] # Very slow growth
    levels_trap = list(range(1, 101)) # Threshold every single length step up to 100
    write_test_case(idx, n_trap, 100, 50, readings_trap, levels_trap)
    idx += 1
    
    # Case 11: TLE Enforcer - Giant Mountain (n=100,000)
    n_giant = 100000
    half = n_giant // 2
    readings_giant = list(range(1, half + 1)) + list(range(half, 0, -1))
    levels_giant = sorted(random.sample(range(1, n_giant), 50))
    write_test_case(idx, n_giant, 50, 50000, readings_giant, levels_giant)
    idx += 1
    
    # Case 12: TLE Enforcer - Sawtooth (n=100,000)
    n_saw = 100000
    readings_saw = []
    for i in range(n_saw):
        if i % 10 == 0:
            readings_saw.append(1000000) # Massive spike every 10 steps
        else:
            readings_saw.append(i % 10) # Small stable panel
    levels_saw = sorted(random.sample(range(1, n_saw), 20))
    write_test_case(idx, n_saw, 20, 20, readings_saw, levels_saw)
    idx += 1

if __name__ == '__main__':
    print("Generating secret test cases...")
    generate_all_cases()
    print("Done! All files written to submission/data/secret/")