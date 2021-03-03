#Baslangic
metin = input("[*] Şifrelenecek metni giriniz:\r\n")
anahtar = input("[*] Anahtarı giriniz:\r\n")

#Adım:1
InitialStateVector = [] #S[i]
TemporaryVector = [] #K[i]
for i in range(256):
    InitialStateVector.append(i)
    TemporaryVector.append(anahtar[i % len(anahtar)])
soru = input("Initial State Vector değeri gösterilsin mi?(e/h)\r\n")
if(soru == "e"):
    print("Initial State Vector:")
    for i in range(256):
        print(InitialStateVector[i], end=" ")

soru = input("\r\nTemporary Vector değeri gösterilsin mi?(e/h)\r\n")
if(soru == "e"):
    print("Temporary Vector:")
    for i in range(256):
        print(TemporaryVector[i], end=" ")

#Adım:2

j = 0
for i in range(256):
    j = (j + InitialStateVector[i] + ord(TemporaryVector[i])) % 256
    deger1 = InitialStateVector[j]
    deger2 =  InitialStateVector[i]
    InitialStateVector[j] = deger2
    InitialStateVector[i] = deger1
print()
soru = input("Permuted State Vector değeri gösterilsin mi?(e/h)\r\n")
if(soru == "e"):
    print("Permuted State Vector:")
    for i in range(256):
        print(InitialStateVector[i], end=" ")
       
#Adım:3
i = 0
j = 0
k=[]
C = []
for l in range(len(metin)):
    i = (i + 1) % 256
    j = (j + InitialStateVector[i])  % 256
    deger1 = InitialStateVector[i]
    deger2 = InitialStateVector[j]
    k.append( InitialStateVector[((InitialStateVector[i] + InitialStateVector[j]) % 256)])

    p = ord(metin[l])
    c = bin(p ^ k[l])
    C.append(int(c,2))

print("\r\n",C,sep="")

