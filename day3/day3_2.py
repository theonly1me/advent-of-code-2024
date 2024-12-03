import re

sample_text="xmul(2,4)&mul[3,7]!^don't()_mul(5,5)+mul(32,64](mul(11,8)undo()?mul(8,5))"
pattern = r"do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\)"
products = []
with open("day3_2.txt", "r") as file:
    matches = re.findall(pattern, file.read())
    processing = True
    for match in matches:
        if match == "do()":
            processing = True
        elif match == "don't()":
            processing = False
        elif processing and match.startswith("mul("):
            nums = re.findall(r"\d{1,3}", match)
            products.append(int(nums[0]) * int(nums[1]))
    print(f"Totals: {sum(products)}")
