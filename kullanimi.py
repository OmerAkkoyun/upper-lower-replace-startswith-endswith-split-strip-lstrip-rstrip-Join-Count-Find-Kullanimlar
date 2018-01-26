a="omer"
print(a.upper())#Büyük harflere çevirir.
#çıktısı:OMER
#--------------------------------------------------------------
b="AHMET"
print(b.lower()) #küçük harflere çevirir.
#çıktısı:ahmet
#--------------------------------------------------------------
c="bababa"
print(c.replace("a","e"))    #a harflerini e ile değiştirdik.
#çıktısı:bebebe

#--------------------------------------------------------------
d="Python"
print(d.startswith("P")) #d değişkeni P ile mi başlıyor?
#Çıktı:True

d="Python"
print(d.startswith("Y")) #d değişkeni Y ile mi başlıyor?
#Çıktı:False

d="Python"
print(d.endswith("on")) #d değişkeni "on" ile mi bitiyor?
#Çıktı:True

d="Python"
print(d.endswith("Y")) #d değişkeni "kon" ile mi bitiyor?
#Çıktı:False
#--------------------------------------------------------------
dizi=("ahmet-mehmet-ayşe-rabia")
print(dizi.split("-")) #tire ye göre bölüp diziye atar.
#çıktısı:['ahmet', 'mehmet', 'ayşe', 'rabia']
#--------------------------------------------------------------
liste=("T","B","M","B")
print(".".join(liste))#birleştirmeye yarar.
#çıktısı: T.B.M.B
#--------------------------------------------------------------
yazi="ahmet eve geç geldi"
print(yazi.count("e"))#yazi içinde kaçtane e harfi var?
#çıktısı : 5

yazi="ahmet eve geç geldi"
print(yazi.count("e",5))#5.indisten sonra saymaya başlasın
#çıktısı : 4
#--------------------------------------------------------------
yazi="ahmet eve geç geldi"
print(yazi.find("a")) #yazi içinde a harfini gördüğü ilk indis?
#çıktısı:0
#--------------------------------------------------------------
yazi="ahmet eve geç geldi"
print(yazi.rfind("e")) #yazi içinde e harfini tersten bakarak gördüğü indis?
#çıktısı:15
#--------------------------------------------------------------

