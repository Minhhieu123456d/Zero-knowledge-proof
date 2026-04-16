import random
import math


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            return False
    return True

print("=== SCHNORR PROTOCOL DEMO (RANDOM CHALLENGE) ===")

while True:
    p = int(input("Nhập số nguyên tố p: "))
    if is_prime(p):
        break
    print("p không phải số nguyên tố, nhập lại!")

while True:
    g = int(input("Nhập phần tử sinh g: "))
    if 1 < g < p:
        break
    print(f"g phải nằm trong khoảng (1, {p}), nhập lại!")

x = int(input("Nhập khóa bí mật x: "))
y = pow(g, x, p)

print("\n[Public key] y =", y)
print("(Server chỉ biết y, KHÔNG biết x)")
print("=" * 40)

num_rounds = int(input("\nNhập số vòng xác thực: "))

success_count = 0

for round_num in range(1, num_rounds + 1):
    print(f"\n--- VÒNG {round_num} ---")


    r = int(input(f"Nhập số ngẫu nhiên r (vòng {round_num}): "))
    R = pow(g, r, p)
    print(f"[Prover] gửi R = {R}")

    c = random.randint(1, p - 1)
    print(f"[Verifier] challenge ngẫu nhiên c = {c}")


    s = int(input(f"Nhập phản hồi s (vòng {round_num}): "))


    left = pow(g, s, p)
    right = (R * pow(y, c, p)) % p
    s_correct = (r + c * x) % (p - 1)

    print(f"\n[Verifier kiểm tra vòng {round_num}]:")
    print(f"Vế trái (g^s mod p) = {left}")
    print(f"Vế phải (R * y^c mod p) = {right}")

    if left == right:
        print(" XÁC THỰC THÀNH CÔNG")
        success_count += 1
    else:
        print("XÁC THỰC THẤT BẠI")
        break

print("\n" + "-" * 40)
if success_count == num_rounds:
    print(f"KẾT QUẢ: {success_count}/{num_rounds} vòng thành công")
    print("KẾT LUẬN: NGƯỜI DÙNG TRUNG THỰC")
else:
    print(f"KẾT QUẢ: {success_count}/{num_rounds} vòng thành công")
    print("KẾT LUẬN: KẺ GIAN LẬN")
