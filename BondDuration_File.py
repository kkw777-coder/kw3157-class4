
def getBondDuration(y, face, couponRate, m, ppy = 1):
     if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    coupon = face * couponRate / ppy
    period = m * ppy
    y = y / 100
     couponPV = 0
for t in range (1, period + 1):
    couponPV += coupon / (1 + y / ppy) ** t
    facePV = face/(1 + y / ppy) ** period
    BondPrice = couponPV + facePV
    BondDuration += (couponPV * t + facePV * period) / BondPrice
    return BondDuration
# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
ppy = 2
    return(8.51)
