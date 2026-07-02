def is_year_leap(year):
    return year % 4 == 0
year = [2023, 2024, 2020]
for y in year:
    result = is_year_leap(y)
    print(f"год {y}: {result}")