year = int(input("Give the year to check the year is leap year or not: "))


if year%4 == 0:
    if year%100==0:
        if(year%400==0):
            print(f"The {year} is leap year")
        else:
            print(f"The {year} is not leap year")
    else:
        print(f"The {year} is leap year")
else:
    print(f"The {year} is not leap year")    
