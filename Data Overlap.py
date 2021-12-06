with open("file1.txt") as f1:
  item1 = f1.readlines()
with open("file2.txt") as f2:
  item2 = f2.readlines()

result = [int(n) for n in item1 if n in item2 ]

print(result)
