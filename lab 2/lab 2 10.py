len=int(input("ENTER THE LENGTH OF RECTANGLE:"))
bre=int(input("ENTER THE BREATH OF RECTANGLE:"))
area=len*bre
per=2*(len+bre)
print("THE AREA IS:",area)
print("THE PERIMETER IS:",per)
if(area>per):
    print("THE AREA IS GREATER THAN PERIMETER")
else:
    print("AREA IS LESS THAN PERIMETER")

