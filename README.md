Uzun zamandır yeni yazı yazmıyorum, bunun asıl sebebi bu aralar WLAN konusunu derinlemesine incelememden kaynaklanıyor. Bilinen bütün şifreleme tekniklerini en ince ayrıntısına kadar anlamaya çalışıyorum. Açıkçası şifreleme konusu çok dikkatimi çekmeye başladı.

Kısaca bir şeyden bahsetmek istiyorum. İnternette pdf'lerini bulduğum kitapları basmak için eve yazıcı, ciltleme makinesi, plastik spriller, cilt kapakları gibi araçlar aldım. Evim şuanda basit bir kırtasiye gibi çalışıyor diyebilirim. Ancak kitaplığım 1 haftada doldu. Tam 10 top A4 harcadım! Ama hala okumak ya da sahip olmak istediğim bir sürü kitap var. Eğer benim gibi bi düşünceniz varsa Amazon Kindle alın. Şimdi onun siparişini verdim ve artık kaynaklarımı sürekli olarak yanımda taşıyacağım. Peki bunu neden anlattım? Aslında WEP Şifrelemeyi araştırırken, şifreleme ile ilgili hiç bir kitap okumadağımı farkettim. Tabiki de türkçe yayınları saymıyorum. Bunun üzerine arayışa girdim ve konu kindle siparişi vermeye kadar dağıldı...

Bu aralar tamamen eskimiş WEP şifrelemesini anlamaya çalışıyorum. *aircrack-ng ye verince kırıyor hocam neden uğraşıyorsun ayrıca ne işine yarayacak* diye bir düşünceniz varsa, kendinize bir iyilik yapın ve beni takip etmeyi bırakın. Bu düşüncedeki insanlar o kadar fazla ki artık bende bir sinir oluşturmaya başladı. Insanlar vakti zamanında bunlarla alakalı yazılar paylaşmış makaleler yazmış konferanslar vermiş güzel ülkemde ne zaman bu seviyeye ulaşacağız merak ediyorum. Bir kaç sene önce TürkTelekom ve Garanti Bankasına düzenlenen DDOS saldırıları sonucu çok güzel tecrüeler edindik. Sanırım her alanda iyi bi hacklenmemiz gerekiyor yoksa akıllanmıyoruz. Herkes güvenlikten konuşuyor ama takip ettiğin siberciler kimler diye sorduğumda 3 kişiden fazla insan sayanı görmedim. Verdikleri isimlerde film kahramanları orası ayrı. Ama herkes tuttuğu takımın ilk 11'ini sayabiliyor. Bu bir gönül işi olmalı sevmiyorsan sivrilmeye çalışma!

Neyse gelelim konumuza RC4 algoritamasının çalışması hakkında size bilgi vermek istiyorum bu algoritam direkt olarak WEP şifrelemede kullanılmaktadır.

<iframe width="100%" height="auto" src="https://www.youtube.com/embed/kfdvlaOD1ig" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>

Yukarıdaki videoda bir animasyon ile bunun nasıl çalıştığı anlatılmış. Aşağıda bunun basit bir python konudu yazdım aşama aşama bakalım.

RC4 içerisinde bir key'e ihtiyaç duyarız ve bu key aracılığı ile metnimizi şifreleriz. İlk olarak kullanıcıdan bunları isteyelim.

```py
#Baslangic
metin = input("[*] Şifrelenecek metni giriniz:\r\n")
anahtar = input("[*] Anahtarı giriniz:\r\n")

```

Daha sonra bir IV (Initial Vector) tanımlaması yapmamız gerekiyor. Bu değer 256 bit uzunluğundadır. 0'dan başlar 255'e kadar gider. RC4 için böylece IV değerimiz hazırdır. İkinci işlem olarak Temporary Vector'u ayarlamamız gerekecektir. Bunun için ilk başta belirlediğimiz Key'i kullanarız. Yine TV değeri 256bit uzunluğunda olacaktır. belirlediğimiz anahar değerinin arka arkaya yazılması ile elde edilir. Aşağıda bunlar python ile nasıl yapabileceğimize bakalım.
```py
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
```

Şimdi yukarıdaki işlemlerin ekran çıktılarına bakalım.
```
PS C:\Users\kuday\OneDrive\Desktop\encrption> py .\rc4.py
[*] Şifrelenecek metni giriniz:
kuday
[*] Anahtarı giriniz:
key
Initial State Vector değeri gösterilsin mi?(e/h)
e
Initial State Vector:
0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 
146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 172 173 174 175 176 177 178 179 180 181 182 183 184 185 186 187 188 189 190 191 192 193 194 195 196 197 198 199 200 201 202 203 204 205 206 207 208 209 210 211 212 213 214 215 216 217 218 219 220 221 222 223 224 225 226 227 228 229 230 231 232 233 234 235 236 237 238 239 240 241 242 243 244 245 246 247 248 249 250 251 252 253 254 255
Temporary Vector değeri gösterilsin mi?(e/h)
e
Temporary Vector:
k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y k e y 
k e y k e y k e y k e y k e y k e y k
```
Harika! Tam da dediğim gibi. Lütfen aşağıdaki fotoğrafa bakınız.
<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/4/44/Wep-crypt-alt.svg/305px-Wep-crypt-alt.svg.png" width="100%" height="auto">

Yukarıdaki görselden de anlaşılacağı gibi IV ile KEY'i RC4 işlemine artık sokmamız gerekmektedir. Bunun sonucunda bir keystream değeri elde edeceğiz. Ve bu keystream daha sonra açık metinle XOR'a sokulacaktır. Python kodları ile devam edelim.

```py
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
```

Yukarıda ne yaptı? IV ve TV değerlerini swaplama işlemine tabii tutuyoruz. Şu ana kadar yaptığımız işleme Key-scheduling algorithm (KSA) denmektedir. Ve genel formülü aşağıdaki gibidir.
```
for i from 0 to 255
    S[i] := i
endfor
j := 0
for i from 0 to 255
    j := (j + S[i] + key[i mod keylength]) mod 256
    swap values of S[i] and S[j]
endfor
```

Bu işlemin sonucu bize aşağıdaki gibi bir çıktı verecektir.
```
Permuted State Vector değeri gösterilsin mi?(e/h)
e
Permuted State Vector:
107 195 95 122 35 161 131 126 255 115 130 227 84 77 214 173 253 234 192 56 100 69 6 15 211 17 228 106 235 129 46 142 39 179 96 29 70 85 203 250 174 25 44 65 187 37 226 62 97 247 33 64 19 114 135 196 23 32 123 87 175 68 59 52 113 78 216 128 120 170 110 2 185 22 190 127 18 104 163 5 248 180 75 172 0 208 57 182 11 92 30 27 159 204 160 105 205 188 31 63 50 176 246 125 153 206 143 181 240 146 36 193 28 124 101 242 55 191 210 138 162 156 186 157 9 184 53 21 155 82 90 71 245 116 222 254 3 76 81 148 230 134 102 237 49 200 166 88 118 66 7 213 178 72 201 47 197 144 24 42 74 220 171 207 51 60 45 209 16 58 194 168 219 251 150 14 67 183 140 61 249 117 133 89 145 79 212 243 151 152 218 108 103 215 241 149 223 167 40 199 136 112 10 111 141 169 109 198 139 244 154 38 12 236 217 137 20 252 189 229 119 221 73 34 177 158 132 231 93 86 224 48 164 91 239 83 98 202 54 13 26 4 1 94 233 225 232 43 165 41 8 80 238 121 99 147
```

Ve Pseudo-random generation algorithm (PRGA) dediğimiz son aşamaya geldik. Artık burda XOR işlemi uygulayarak açık metnimizi şifrelemiş olacağız. Videoya tekrar baktığınızda Hello World! kelimesini şifrelediğini göreceksiniz. Dikkat ettiyseniz l harflerinin şifreli değerleri birbirinden farklıdır. Bu sayede frekans analizi yapılamayacak bir güven ortamı oluşturulur ayrıca her metin için PV değerinin sabit olmasıda bir o kadar güvensizdir. Zaten başta dediğim gibi artık kullanılmayan bir şifreleme. PRGA işleminin genel formülü aşağıda verilmiştir.

```
i := 0
j := 0
while GeneratingOutput:
    i := (i + 1) mod 256
    j := (j + S[i]) mod 256
    swap values of S[i] and S[j]
    K := S[(S[i] + S[j]) mod 256]
    output K
endwhile
```
Yukarıdaki işlemin python kodu ise aşağıda verilmiştir.
```py
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
```
En son olarak alacağımız çıktı aşağıdaki gibidir.
```
[96, 25, 80, 140, 93]
```

Tebrikler kuday ifadesini anahtar değeri key olan bir anahtarla RC4 ile şifreledik ve ascii karşılıklarını elde ettik!

Python kodunun için tıklayınız.

