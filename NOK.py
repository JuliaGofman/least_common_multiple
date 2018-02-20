a, b = int(input()), int(input())
d = max(a, b)
while d % a != 0 or d % b != 0:
      d += 1
print(d)