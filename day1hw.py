price_rice = 45
price_sugar = 40
price_oil = 130

qty_rice = 3
qty_sugar = 2.5
qty_oil = 1.8

totalprice_rice = price_rice * qty_rice
totalprice_sugar = price_sugar * qty_sugar
totalprice_oil = price_oil * qty_oil

print("Total price of rice :" , totalprice_rice)
print("Total price of sugar :" , totalprice_sugar)
print("Total price of oil :" , totalprice_oil)

total_bill = totalprice_rice + totalprice_sugar + totalprice_oil

print("Total bill is :" , total_bill)

tot_bill_int = int(total_bill)
tot_bill_str = str(tot_bill_int)

print( "Total_billstr :",  tot_bill_str)

import random

delivery_charge = random.randint(5, 10)

final_bill = tot_bill_int + delivery_charge

print("Final bill is :" , final_bill)


