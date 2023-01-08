import json

INPUT_FILE = "input.csv"


with open(INPUT_FILE, "r") as f:

    l1 = []
    l2 = []
    lines = []

    dict3 = {}
    count = 0

    for line in f:
         count = count + 1
         if count < 2:
          for i in range(len(line.split(",")) - 1):
            k = line.split(",")[i]
            l1.append(k)
         if count >= 2:
          for i in range(len(line.split(","))):
            t = line.split(",")[i]
            l2.append(t)

dict1 = {}
for char in l1:
    for k in range(1):
        dict1[char] =l2[k]

lines.append(dict1)
print(json.dumps(lines))

# TODO реализовать конвертер из csv в json

