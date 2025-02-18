

def getBondPrice_E(face, couponRate, yc):
    if ppy == 1:
        x = 2170604
    if ppy == 2:
        x = 2171686
    coupon = face * couponRate / ppy
    period = m * ppy
for y in range (1, 4)
    y = y / 100
     couponPV = 0
for t in range (1, period + 1):
    couponPV += coupon / (1 + y / ppy) ** t
    BondPrice = 0
    BondPrice = couponPV + face/(1 + y / ppy) ** period
    return BondPrice
# Test values
y = 0.03
face = 2000000
couponRate = 0.04
m = 10
ppy = 1
ppy = 2
