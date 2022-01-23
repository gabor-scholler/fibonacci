a, b, limit = 0, 1, int(input("Limit: ")) + 1

while a < limit:
  print(a)
  a, b = b, a + b
