from collections import Counter

left = []
right = []
with open("day1_1.txt", 'r') as file:
    lines = file.readlines()
    for line in lines:
      line = line.strip()
      n1, n2 = map(int, line.split())
      left.append(n1)
      right.append(n2)
counts = Counter(right)
similarityScore = [counts[num] * num for num in left]
print("\nsimilarity score:", sum(similarityScore))
