# ===================== &nbsp;program constants
TAX_RATE=0.0875
TIP_RATE=0.18

# =============================== data input
mealAmt=float(input('please input the amount of the meal '))

# ======================== &nbsp;calculations
taxAmt=mealAmt * TAX_RATE

# ============================= print results
print(f'meal cost is {mealAmt: .2f}')
print(f'tax amount is &nbsp;{taxAmt: .2f}')
print(f'tip amount is {tipAmt: .2f}')
