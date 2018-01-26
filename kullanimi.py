a="omer"
print(a.upper())#Büyük harflere çevirir.
#çýktýsý:OMER
#--------------------------------------------------------------
b="AHMET"
print(b.lower()) #küçük harflere çevirir.
#çýktýsý:ahmet
#--------------------------------------------------------------
c="bababa"
print(c.replace("a","e"))    #a harflerini e ile deðiþtirdik.
#çýktýsý:bebebe

#--------------------------------------------------------------
d="Python"
print(d.startswith("P")) #d deðiþkeni P ile mi baþlýyor?
#Çýktý:True

d="Python"
print(d.startswith("Y")) #d deðiþkeni Y ile mi baþlýyor?
#Çýktý:False

d="Python"
print(d.endswith("on")) #d deðiþkeni "on" ile mi bitiyor?
#Çýktý:True

d="Python"
print(d.endswith("Y")) #d deðiþkeni "kon" ile mi bitiyor?
#Çýktý:False
#--------------------------------------------------------------
dizi=("ahmet-mehmet-ayþe-rabia")
print(dizi.split("-"))
#çýktýsý:['ahmet', 'mehmet', 'ayþe', 'rabia']
#--------------------------------------------------------------
liste=("T","B","M","B")
print(".".join(liste))#birleþtirmeye yarar.
#çýktýsý: T.B.M.B
#--------------------------------------------------------------
yazi="ahmet eve geç geldi"
print(yazi.count("e"))#yazi içinde kaçtane e harfi var?
#çýktýsý : 5

yazi="ahmet eve geç geldi"
print(yazi.count("e",5))#5.indisten sonra saymaya baþlasýn
#çýktýsý : 4
#--------------------------------------------------------------
yazi="ahmet eve geç geldi"
print(yazi.find("a")) #yazi içinde a harfini gördüðü ilk indis?
#çýktýsý:0
#--------------------------------------------------------------
yazi="ahmet eve geç geldi"
print(yazi.rfind("e")) #yazi içinde e harfini tersten bakarak gördüðü indis?
#çýktýsý:15
#--------------------------------------------------------------

