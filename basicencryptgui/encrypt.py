betuk=["a","á","b","c","d","e","é","f",
       "g","h","i","í","j","k","l","m",
       "n","o","ó","ö","ő","p","q","r",
       "s","t","u","ú","ü","ű","v","z",
       "y"," ","\n"]
def encrypt(titkos):
    output = ""
    for i in titkos:
        for j in range(len(betuk)):
            if i.lower() == betuk[j]:
                betu =[int(j/8)+1,j%8+1]
                for k in betu:
                    output += str(k)
    return(output)
def decrypt(input):
    szo = ""
    i = 0
    while i < len(input):
        betu = betuk[(int(input[i])*8+int(input[i+1])-9)]
        i += 2
        szo += betu
        
    return(szo)

swap = False
def modeswap(x):
    globals()['swap'] = True    
    print(swap)
modeswap('asd')
"""
betuk=["a","á","b","c","d","e","é","f",
       "g","h","i","í","j","k","l","m",
       "n","o","ó","ö","ő","p","q","r",
       "s","t","u","ú","ü","ű","v","z", " "]
szo = input("adja meg a szót amit titkositani kiván: ")
kulcs = int(input("adja meg a kulcsor: "))
titkos = ""
if kulcs >= len(betuk):
    kulcs = kulcs%33

for i in szo:
    if betuk.index(i)+kulcs>= 33:
        titkos += betuk[betuk.index(i)+kulcs-33]
    else:
        titkos += betuk[betuk.index(i)+kulcs]
print(titkos)

felold = ""
feloldokulcs = int(input("adja meg a kulcsot: "))
if feloldokulcs >= len(betuk):
    feloldokulcs = feloldokulcs%33
for i in titkos:
    if betuk.index(i)+33-feloldokulcs <= 33:
        felold += betuk[betuk.index(i)+33-feloldokulcs]
    else:
        felold += betuk[betuk.index(i)-feloldokulcs]
print(felold)
"""