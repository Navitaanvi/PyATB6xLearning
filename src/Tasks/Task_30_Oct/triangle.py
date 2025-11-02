def triangle(side1, side2, side3):
    if side1 > 0 and side2 > 0 and side3 > 0:
        if (side1 + side2 > side3) and (side2 + side3 > side1) and (side3 + side1 > side2):
            if side1 == side2 == side3:
                print("Equilateral triangle")
            elif side1 == side2 or side2 == side3 or side3 == side1:
                print("Isosceles triangle")
            else:
                print("Scalene triangle")
        else:
            print("not a valid triangle")
    else:
        print("sides must be positive")


triangle(2, 3, 4)
triangle(4, 4, 4)
triangle(3, 4, 4)
triangle(2, -2, 3)
triangle(2,2,4)