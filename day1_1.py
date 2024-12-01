left = []
right = []
with open("day1_1.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()
      n1, n2 = map(int, line.split())
      left.append(n1)
      right.append(n2)
left.sort()
right.sort()
distances = [abs(a-b) for a,b in zip(left, right)]
print("\ntotal distance:", sum(distances))
