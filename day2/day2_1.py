safe = 0
with open("day2_1.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()
      line_list = list(map(int, line.split()))
      is_ordered = all(line_list[i] > line_list[i+1] for i in range(len(line_list) - 1)) or \
        all(line_list[i] < line_list[i+1] for i in range(len(line_list) - 1))
      has_valid_diffs = all(1 <= abs(line_list[i] - line_list[i+1]) <= 3 for i in range(len(line_list) - 1))
      if is_ordered and has_valid_diffs:
        safe += 1
print(f"Safe: {safe}")
