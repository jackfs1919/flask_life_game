# s = input().strip()
s = ['A', 'O', 'O', 'O', 'Z', 'A', 'O', 'Z']
a = [i for i, c in enumerate(s) if c == 'A']
z = [i for i, c in enumerate(s) if c == 'Z']
distances = [abs(i - j) for i in a for j in z]
print(min(distances) if distances else -1)
print(a, z)
