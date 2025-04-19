def getTriNumber(n):
    return n * (n + 1) // 2

def isqrt(n):
    """Integer square root using binary search."""
    low = 1
    high = n
    while low <= high:
        mid = (low + high) // 2
        if mid * mid <= n:
            low = mid + 1
        else:
            high = mid - 1
    return high

def unpair(P):
    S = isqrt(2 * P) 
    
    while True:
        T_S = getTriNumber(S)
        T_S_plus_1 = getTriNumber(S + 1)
        
        if T_S <= P < T_S_plus_1:
            break
        elif P >= T_S_plus_1:
            S += 1
        else:
            S -= 1
    
    n2 = P - T_S
    n1 = S - n2
    return (n1, n2)

def unpair_array(arr):
    result = []
    for num in arr:
        n1, n2 = unpair(num)
        result.append(n1)
        result.append(n2)
    return result

encoded = 4036872197130975885183239290191447112180924008343518098638033545535893348884348262766810360707383741794721392226291497314826201270847784737584016

current = [encoded]
for i in range(6):
    current = unpair_array(current)
    print(f"Step {i+1}: Length = {len(current)}")

flag_bytes = []
for byte in current:
    if byte == 0:
        break
    flag_bytes.append(byte)

flag = ''.join([chr(b) for b in flag_bytes])
print("Flag:", flag)
