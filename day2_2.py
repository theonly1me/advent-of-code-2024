def is_safe(line_list):
    if len(line_list) < 2:
        return False
    is_ordered = all(line_list[i] > line_list[i+1] for i in range(len(line_list) - 1)) or \
      all(line_list[i] < line_list[i+1] for i in range(len(line_list) - 1))
    has_valid_diffs = all(1 <= abs(line_list[i] - line_list[i+1]) <= 3 for i in range(len(line_list) - 1))
    return is_ordered and has_valid_diffs

safe = 0
with open("day2_2.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()
      line_list = list(map(int, line.split()))
      if is_safe(line_list):
        safe += 1
      else:
         for x in range(len(line_list)):
            sublist = line_list[:x] + line_list[x + 1:]
            if is_safe(sublist):
                safe += 1
                break
print(f"Safe: {safe}")
