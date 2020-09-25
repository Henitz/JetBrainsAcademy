money = int(input())
if money >= 6769:
    animals = money // 6769
    print(str(animals) + " sheep")
elif money >= 3848:
    animals = money // 3848
    if animals > 1:
        print(str(animals) + " cows")
    else:
        print(str(animals) + " cow")
elif money >= 1296:
    animals = money // 1296
    if animals > 1:
        print(str(animals) + " pigs")
    else:
        print(str(animals) + " pig")
elif money >= 678:
    amimals = money // 678
    if amimals > 1:
        print(str(amimals) + " goats")
    else:
        print(str(amimals) + " goat")
elif money >= 23:
    animals = money // 23
    if animals > 1:
        print(str(animals) + " chickens")
    else:
        print(str(animals) + " chicken")
else:
    print("None")