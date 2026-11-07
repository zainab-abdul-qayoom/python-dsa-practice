
weight = int(input("Weight: "))
pound_or_weight = input('(L)bs OR (K)g: ')

lower_case = pound_or_weight.lower()

if lower_case == 'l':
    w_in_kg = 0.453 * weight
    print(f"You're {w_in_kg} kilos")

else:
    w_in_pounds = 2.205 *  weight
    print(f"You're {w_in_pounds} Pounds")

     

