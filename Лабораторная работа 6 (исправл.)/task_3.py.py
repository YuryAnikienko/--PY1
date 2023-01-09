OUTPUT_FILE = "output.csv"

# TODO реализовать функцию to_csv_file
def to_csv_file (filename, headers, rows, delimiter, new_line):

    for t in range(0, len(headers)-1):
          print(headers[t]+",",end = "")
    print(headers[len(headers)-1])

    for i in range(0, len(data)):
        inlist = data[i]
        for k in range(0, len(inlist)-1):
            print(inlist[k]+",", end = "")
        print(inlist[len(inlist)-1])

    with open(OUTPUT_FILE, "w") as f:
        for t in range(0, len(headers)-1):
            f.write(f"{headers[t]}"+",")
        f.write(f"{headers[len(headers)-1]}")
    with open(OUTPUT_FILE, "a") as f:
        for i in range(0, len(data)):
            inlist = data[i]
            f.write(f"\n")
            for k in range(0, len(inlist)-1):
                f.write(f"{inlist[k]}"+",")
            f.write(f"{inlist[len(inlist)-1]}")

headers_list = ['longitude', 'latitude', 'housing_median_age', 'total_rooms', 'total_bedrooms', 'population', 'households', 'median_income', 'median_house_value']

data = [ ['-122.050000', '37.370000', '27.000000', '3885.000000', '661.000000', '1537.000000', '606.000000', '6.608500', '344700.000000'],
    ['-118.300000', '34.260000', '43.000000', '1510.000000', '310.000000', '809.000000', '277.000000', '3.599000', '176500.000000'],
    ['-117.810000', '33.780000', '27.000000', '3589.000000', '507.000000', '1484.000000', '495.000000', '5.793400', '270500.000000'],
    ['-118.360000', '33.820000', '28.000000', '67.000000', '15.000000', '49.000000', '11.000000', '6.135900', '330000.000000'],
]

to_csv_file (OUTPUT_FILE, headers_list, data, "", "\n")

# TODO вызвать функцию to_csv_file и записать данные в файл


print(dict7)
print(ll)
for char2 in l2:
    for char1 in l1:
        dict1[char1] = l2[i]
        lc.append(dict1)

print(json.dumps(lines))
print(json.dumps(lc))


lines.append(dict1)


lin1 = "tttb"
for i in [len([1, 2, 3])]:
    linn = lin1.strip("b")
    print(linn)


 for i in range(len(line.split(",")), len(line.split(","))):
                n = line.split(",")[i].rstrip()
                n1 = n.strip("\n")
                print(n1)

print(e1)
for i in range(len(line.split(",")), len(line.split(","))):
    g = line.split(",")[i].rstrip()
    g1 = g.strip("\n")
    print(g1)

 print(l1)
        print(l2)
        print(l3)
        print(l4)
        print(l5)
