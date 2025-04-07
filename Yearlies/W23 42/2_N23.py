def IterativeCalculate(Number):
    ToFind = Number
    Total = 0

    while Number != 0:
        if ToFind % Number == 0:
            Total = Total + Number
        
        Number = Number - 1
    
    return Total

print(IterativeCalculate(10))

