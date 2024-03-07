PROCENT = 0.1


def bank(dep, year):
    for i in range(year):
        dep = dep + (dep * PROCENT)
    return dep


print(bank(dep=10000, year=5))