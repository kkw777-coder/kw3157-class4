

def getBondPrice(y, face, couponRate, m, ppy=1):
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    coupon = face * couponRate / ppy
    period = m * ppy
    for t in range (1,period+1):
        couponPV += coupon / (1+m/ppy)^t
    BondPrice += couponPV + face/(1+m/ppy)^period
    return BondPrice
