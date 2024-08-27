import random
listpi = []
for i in range(100):
    list = []
    for i in range(100):
        list.append(random.randint(0,32768))
    sorted(list)
    def Lnko(a, b):
        if a == b:
            return a
        if b < a:
            a, b = b, a
        while (0 < a):
            a, b = b % a, a
        return b
    parok = []
    for i in range(len(list)):
        for j in range(i,len(list)):
            if sorted([list[i],list[j]]) not in parok and list[i] != list[j]:
                parok.append(sorted([list[i],list[j]]))
    db = 0
    for j in parok:
        if Lnko(j[0],j[1]) == 1:
            db += 1
    pi = (6*len(parok)/db)**0.5
    listpi.append(pi)
print(sum(listpi)/len(listpi))