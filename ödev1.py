def GelirHesapla(finansmanGelir,pazarGelir,kiraGelir):
    return(finansmanGelir+pazarGelir+kiraGelir)
def GiderHesapla(ucret,finansmanGider,pazarGider,kiraGider,muhasebeGider):
    return(ucret+finansmanGider,pazarGider,kiraGider,muhasebeGider)
gelirler=int(input("Gelirleri giriniz."))
giderler=int(input("Giderleri giriniz."))
if gelirler-giderler>1000:
    print("İşletme kardadır.")
else:
    print("İşletme zarardadır.")
