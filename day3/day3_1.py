import re

pattern = r"mul\((\d{1,3}),(\d{1,3})\)"
with open("day3_1.txt", "r") as file:
    text = file.read()
    matches = re.findall(pattern, text)
    print(f"Totals: {sum([int(num1) * int(num2) for num1, num2 in matches])}")
