import sys

def verify():
    lines = sys.stdin.readlines()
    clean_lines = [line.strip() for line in lines if line.strip() != ""]
    if len(clean_lines) != 4:
        sys.exit(f"Error: Expected exactly 4 lines of data, found {len(clean_lines)}.")
        
    # n and k
    l1 = clean_lines[0].split()
    if len(l1) != 2:
        sys.exit(f"Error: Line 1 must have exactly 2 integers. Found {len(l1)}.")
    n, k = map(int, l1)
    
    assert 1 <= n <= 10**5, f"n={n} is out of bounds (1 to 10^5)"
    assert 1 <= k <= 10**5, f"k={k} is out of bounds (1 to 10^5)"
    
    # limit
    l2 = clean_lines[1].split()
    if len(l2) != 1:
        sys.exit(f"Error: Line 2 must have exactly 1 integer. Found {len(l2)}.")
    limit = int(l2[0])
    assert 1 <= limit <= 10**9, f"limit={limit} is out of bounds (1 to 10^9)"
    
    # stress readings array
    l3 = clean_lines[2].split()
    if len(l3) != n:
        sys.exit(f"Error: Line 3 must have exactly {n} integers. Found {len(l3)}.")
    for x in l3:
        val = int(x)
        assert 1 <= val <= 10**9, f"Stress reading {val} is out of bounds (1 to 10^9)"
        
    # 5. levels array
    l4 = clean_lines[3].split()
    if len(l4) != k:
        sys.exit(f"Error: Line 4 must have exactly {k} integers. Found {len(l4)}.")
    
    prev_level = 0
    for x in l4:
        val = int(x)
        assert 1 <= val <= n, f"Level {val} is out of bounds (must be <= n)"
        assert val > prev_level, f"Levels must be strictly increasing. {val} is not > {prev_level}"
        prev_level = val

    sys.exit(42)

if __name__ == '__main__':
    try:
        verify()
    except AssertionError as e:
        sys.exit(str(e))
    except ValueError as e:
        sys.exit(f"Value error (non-integer found): {e}")