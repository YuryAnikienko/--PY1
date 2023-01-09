import json

INPUT_FILE = "input.csv"

from pprint import pprint

def csv_to_listdict(filename):

    with open(INPUT_FILE, "r") as f:

        l1 = []
        l2 = []
        l3 = []
        l4 = []
        l5 = []
        l = []
        ll = []
        count = 0

        for line in f:
            count = count + 1
            if count == 1:
                for i in range(len(line.split(","))-1):
                    k = line.split(",")[i]
                    l1.append(k)
                for i in range(len(line.split(","))-1, len(line.split(","))):
                    e = line.split(",")[i].rstrip()
                    e1 = e.strip("\n")
                    l1.append(e1)

            if count == 2:
                for i in range(len(line.split(","))-1):
                    t = line.split(",")[i]
                    l2.append(t)
                for i in range(len(line.split(","))-1, len(line.split(","))):
                    e = line.split(",")[i].rstrip()
                    e1 = e.strip("\n")
                    l2.append(e1)

            if count == 3:
                for i in range(len(line.split(","))-1):
                    t = line.split(",")[i]
                    l3.append(t)
                for i in range(len(line.split(","))-1, len(line.split(","))):
                    e = line.split(",")[i].rstrip()
                    e1 = e.strip("\n")
                    l3.append(e1)

            if count == 4:
                for i in range(len(line.split(","))-1):
                    u = line.split(",")[i]
                    l4.append(u)
                for i in range(len(line.split(","))-1, len(line.split(","))):
                    e = line.split(",")[i].rstrip()
                    e1 = e.strip("\n")
                    l4.append(e1)

            if count == 5:
                for i in range(len(line.split(","))-1):
                    t3 = line.split(",")[i]
                    l5.append(t3)
                for i in range(len(line.split(","))-1, len(line.split(","))):
                    e = line.split(",")[i].rstrip()
                    e1 = e.strip("\n")
                    l5.append(e1)


    dict1 = {}
    dict2 = {}
    dict3 = {}
    dict4 = {}

    for i in range(len(line.split(","))):
        dict1[l1[i]] = l2[i]
    ll.append(dict1)
    for i in range(len(line.split(","))):
        dict2[l1[i]] = l3[i]
    ll.append(dict2)
    for i in range(len(line.split(","))):
        dict3[l1[i]] = l4[i]
    ll.append(dict3)
    for i in range(len(line.split(","))):
        dict4[l1[i]] = l5[i]
    ll.append(dict4)

    print(json.dumps((ll), indent = 4))


csv_to_listdict(INPUT_FILE)


# TODO реализовать конвертер из csv в json


