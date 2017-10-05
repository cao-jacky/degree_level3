val_one = float(raw_input("What is your first value? "))
if val_one < 0:
    print "You have entered a negative number for your first value, it has been converted to a positive."
    val_one = val_one * (-1)

val_two = float(raw_input("What is your second value? "))
if val_two < 0:
    print "You have entered a negative number for your second value, it has been converted to a positive."
    val_two = val_two * (-1)

area = val_one * val_two
print "Area of your rectangle is", '%g' % (area) 
