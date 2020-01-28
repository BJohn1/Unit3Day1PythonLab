# exercise-04 What kind of Triangle?

# Write the code that:
# 1. Prompts the user to enter the three lengths of a triangle (one at a time):
#      Enter the lengths of three side of a triangle:
#      a: 
#      b:
#      c:
# 2. Write the code that determines if the triangle is:
#      equalateral - all three sides are equal in length
#      scalene - all three sides are unequal in length
#      isosceles - two sides are the same length
# 3. Print a message such as:
#      - A triangle with sides of <a>, <b> & <c> is a <type of triangle> triangle


    sidea = input("Enter the length of the first side of a triangle: ").lower()
sideb = input("Enter the length of the second side of a triangle: ").lower()
sidec = input("Enter the length of the third side of a triangle: ").lower()
sum=int(sidea)+int(sideb)+int(sidec)

if sum/(int(sidea)) == 3:
    print(f"A triangle with sides of {sidea}, {sideb}, & {sidec} is an equilateral triangle")
elif int(sidea) != int(sideb):
    if int(sidea) != int(sidec):
        if int(sidec) != int(sideb):
            print(f"A triangle with sides of {sidea}, {sideb}, & {sidec} is a scalene triangle")
elif int(sidea) == int(sideb) or int(sidec) == int(sideb) or int(sidea) == int(sidec):
    print(f"A triangle with sides of {sidea}, {sideb}, & {sidec} is an isosceles triangle")

        



