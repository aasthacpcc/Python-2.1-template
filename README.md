Complete the python program:
Calculate total cost of meal including sales tax and tip
Prompt for cost of meal
Perform the calculations for tax
Perform the calculations for tip
Display the results
Sales tax rate – 8.75%
Tip is 18%
Sample output below:

Meal cost is 25.73
Tax amount is  2.25
Tip amount is 4.63
Total cost of meal 32.61

=================== &nbsp;copy program below this line ========================

# student name 2024FA ch02_lab01
'''
This program will accept input of a meal cost and then:
1. Calculate the sales amount
2. Calculate the tip amount
3. Print the results to include: meal amount, tip amount, tax amount, total cost

'''
# ===================== program constants
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
