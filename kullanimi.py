a="omer"
print(a.upper())#B�y�k harflere �evirir.
#��kt�s�:OMER
#--------------------------------------------------------------
b="AHMET"
print(b.lower()) #k���k harflere �evirir.
#��kt�s�:ahmet
#--------------------------------------------------------------
c="bababa"
print(c.replace("a","e"))    #a harflerini e ile de�i�tirdik.
#��kt�s�:bebebe

#--------------------------------------------------------------
d="Python"
print(d.startswith("P")) #d de�i�keni P ile mi ba�l�yor?
#��kt�:True

d="Python"
print(d.startswith("Y")) #d de�i�keni Y ile mi ba�l�yor?
#��kt�:False

d="Python"
print(d.endswith("on")) #d de�i�keni "on" ile mi bitiyor?
#��kt�:True

d="Python"
print(d.endswith("Y")) #d de�i�keni "kon" ile mi bitiyor?
#��kt�:False
#--------------------------------------------------------------
dizi=("ahmet-mehmet-ay�e-rabia")
print(dizi.split("-"))
#��kt�s�:['ahmet', 'mehmet', 'ay�e', 'rabia']
#--------------------------------------------------------------
liste=("T","B","M","B")
print(".".join(liste))#birle�tirmeye yarar.
#��kt�s�: T.B.M.B
#--------------------------------------------------------------
yazi="ahmet eve ge� geldi"
print(yazi.count("e"))#yazi i�inde ka�tane e harfi var?
#��kt�s� : 5

yazi="ahmet eve ge� geldi"
print(yazi.count("e",5))#5.indisten sonra saymaya ba�las�n
#��kt�s� : 4
#--------------------------------------------------------------
yazi="ahmet eve ge� geldi"
print(yazi.find("a")) #yazi i�inde a harfini g�rd��� ilk indis?
#��kt�s�:0
#--------------------------------------------------------------
yazi="ahmet eve ge� geldi"
print(yazi.rfind("e")) #yazi i�inde e harfini tersten bakarak g�rd��� indis?
#��kt�s�:15
#--------------------------------------------------------------

