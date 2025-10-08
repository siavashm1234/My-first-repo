weight = input(f"what is your weight")
number_weight=int(weight)
unit= input(f"(K)ilo or (L)bs?")

if unit.upper() != "k" and unit.upper() != "L":
    print( "i dont get it")
elif unit.upper() == "K":
    pound=number_weight * 2.2
    print(pound)
elif unit.upper() == "l":
    kilo=number_weight/ 2.2
    print(kilo)
else:
    print(f"i dont get it")
