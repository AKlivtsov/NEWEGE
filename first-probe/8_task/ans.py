import itertools

volves = "ИЕОА"
not_volves = "ГПРБЛ"


def check(comb: str) -> bool:
    if comb[0] in volves:
        return False

    if comb[-1] in volves:
        return False

    for i in range(1, 5):
        if (
            (comb[i - 1] in not_volves)
            and (comb[i] in volves)
            and (comb[i + 1] in not_volves)
        ):
            return False

    return True


c = 0
for comb in itertools.product("ГИПЕРБОЛА", repeat=6):
    comb = "".join(comb)
    if check(comb):
        c += 1

print(c)  # 68025
