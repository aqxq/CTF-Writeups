from Crypto.Util.number import inverse, long_to_bytes
import math

e_pub = 58271
d_pub = 16314065939355844497428646964774413938010062495984944007868244761330321449198604198404787327825341236658059256072790190934480082681534717838850610633320375625893501985237981407305284860652632590435055933317638416556532857376955427517397962124909869006289022084571993305966362498048396739334756594170449299859
N = 119082667712915497270407702277886743652985638444637188059938681008077058895935345765407160513555112013190751711213523389194925328565164667817570328474785391992857634832562389502866385475392702847788337877472422435555825872297998602400341624700149407637506713864175123267515579305109471947679940924817268027249
c = 107089582154092285354514758987465112016144455480126366962910414293721965682740674205100222823439150990299989680593179350933020427732386716386685052221680274283469481350106415150660410528574034324184318354089504379956162660478769613136499331243363223860893663583161020156316072996007464894397755058410931262938
e_priv = 65537

k = (e_pub * d_pub - 1) // N  
phi_approx = (e_pub * d_pub - 1) // k

sum_pq = N + 1 - phi_approx
discriminant = sum_pq**2 - 4 * N
if discriminant < 0:
    print("Discriminant is negative, adjusting k...")
    for delta in [-1, 1]:
        k_new = k + delta
        if k_new == 0:
            continue
        phi_approx_new = (e_pub * d_pub - 1) // k_new
        sum_pq_new = N + 1 - phi_approx_new
        discriminant_new = sum_pq_new**2 - 4 * N
        if discriminant_new >= 0:
            sum_pq = sum_pq_new
            discriminant = discriminant_new
            break
    else:
        print("Failed to find suitable k")
        exit()

sqrt_discriminant = math.isqrt(discriminant)
if sqrt_discriminant**2 != discriminant:
    print("Discriminant is not a perfect square, adjusting k...")
    for delta in range(-5, 6):
        if delta == 0:
            continue
        k_new = k + delta
        if k_new == 0:
            continue
        phi_approx_new = (e_pub * d_pub - 1) // k_new
        sum_pq_new = N + 1 - phi_approx_new
        discriminant_new = sum_pq_new**2 - 4 * N
        if discriminant_new >= 0:
            sqrt_disc_new = math.isqrt(discriminant_new)
            if sqrt_disc_new**2 == discriminant_new:
                sum_pq = sum_pq_new
                discriminant = discriminant_new
                sqrt_discriminant = sqrt_disc_new
                break
    else:
        print("Failed to find suitable k")
        exit()

p = (sum_pq + sqrt_discriminant) // 2
q = (sum_pq - sqrt_discriminant) // 2

if p * q != N:
    print("Factorization failed: p * q != N")
    exit()

print(f"Found p: {p}")
print(f"Found q: {q}")

phi = (p - 1) * (q - 1)
d_priv = inverse(e_priv, phi)

m = pow(c, d_priv, N)
flag = long_to_bytes(m)
print(f"Decrypted flag: {flag.decode()}")
