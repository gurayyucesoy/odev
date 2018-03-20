#dbs= Dönem başı stoğu
#ks= Koltuk sayısı
#ys= Yatak sayısı
#ds= Dolap sayısı
#dss= Dönem sonu stoğu
#ort= Ortalama stok
def dbs(ks,ys,ds):
    global dbs
    dbs= ks+ys+ds
    return dbs
a = int(input("Koltuk sayısını giriniz:"))
b = int(input("Yatak sayısını giriniz:"))
c = int(input("Dolap sayısını giriniz:"))
d=dbs(a,b,c)
print("Dönem başı stoğunuz:",dbs)
def dss(ks,ys,ds):
    global dss
    dss= ks+ys+ds
    return dss
x = int(input("Koltuk sayısını giriniz:"))
y = int(input("Yatak sayısını giriniz:"))
z = int(input("Dolap sayısını giriniz:"))
v=dss(x,y,z)
print("Dönem sonu stoğunuz:",dss)
hesapla=(dbs + dss) / 2
ort=format(hesapla)
print("Ortalama stoğunuz:",ort)
