def year(n):
    
    return f"Год {n} Высокосный?: {n % 4 == 0}"


print(year(2024))
print(year(2023))
print(year(2022))