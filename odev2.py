def Kullanilabilirlik(PlanlanmisUretimSüresi,PlansizDurus,PlanlanmisUretimSuresi):
    return(PlanlanmisUretimSuresi-PlansizDurus)/(PlanlanmisUretimSuresi)
def Performans(StandartCevrimZamani,UretimMiktari,PlanlanmisUretimSuresi,PlansizDurus):
    return(StandartCEvrimZamani*UretimMiktari)/(PlanmisUretimSuresi-PlansizDurus)
def Kalite(SaglamUrunMiktari,ToplamUretimMiktari):
    return(SaglamUrunMiktari)/(ToplamUretimMiktari)

def OEE(Kullanilabilirlik,Performans,Kalite):
    return(Kullanilabilirlik*Performans*Kalite)/100

