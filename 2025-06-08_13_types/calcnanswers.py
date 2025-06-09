# -- task 56
# print(bin(192)[2:])
# print(bin(208)[2:])
# print(int("11000000", 2))  # 192

# -- task 61
# print(bin(96)[2:])
# print(bin(123)[2:])
# print(int("11100000", 2))  # 224

# -- task 47
# print(bin(139)[2:])
# print(bin(154)[2:])
# print(8 * 3 + 3)  # 27 + 1

# -- task 65
# print("0" + bin(95)[2:])
# print(bin(224)[2:])
# print(int("01000000", 2))  # 64

# -- task 69
# print(f"0{bin(98)[2:]}.0{bin(81)[2:]}.{bin(154)[2:]}.{bin(192)[2:]}")
# print(f"{bin(255)[2:]}.{bin(252)[2:]}.00000000.00000000")
# print(
#     int("1100010", 2), int("1010011", 2), int("11111111", 2), int("11111110", 2)
# )  # 9883255254

# -- task 19
# print(bin(122)[2:], bin(159)[2:], bin(136)[2:], bin(144)[2:])
# print(bin(248)[2:])

# from itertools import product

# c = 0
# for comb in product("01", repeat=3):
#     comb = "".join(comb)
#     comb = "1" * 15 + comb

#     if comb.count("1") % 4 != 0:
#         c += 1

# print(c)  # 5

# -- task 20
# print(bin(112)[2:], bin(160)[2:], bin(0)[2:], bin(0)[2:])  # 1 - 5
# print(bin(240)[2:])
# from itertools import product

# c = 0
# for comb in product("01", repeat=20):
#     comb = "".join(comb)
#     comb = "1" * 5 + comb

#     if comb.count("1") % 5 != 0:
#         c += 1

# print(c)  # 832810

# -- task 22
# print(bin(157)[2:], bin(220)[2:], bin(183)[2:], bin(0)[2:])
# print(bin(157)[2:], bin(220)[2:], bin(184)[2:], bin(0)[2:])
# print(bin(255)[2:], bin(255)[2:], bin(240)[2:], bin(0)[2:])
# from itertools import product

# c = 0
# for comb in product("01", repeat=12):
#     comb = "".join(comb)
#     comb = "1" * 13 + comb

#     if comb.count("1") == 15 and comb[-1] != "1":
#         print(comb)
#         c += 1

# print(c)  # 55
