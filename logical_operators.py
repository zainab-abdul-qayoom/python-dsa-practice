has_good_credit = True
has_high_income = False
has_criminal_record = True

# AND Operator
if has_good_credit and has_high_income:
    print("Eligible for loan")

# OR Operator
if has_high_income or has_good_credit:
    print("Eligible for loan")

# Not Operator (inverses the boolean)
if has_high_income and not has_high_income:
    print("Eligible for loan")