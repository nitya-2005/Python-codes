def are_points_collinear(x1, y1, x2, y2, x3, y3):
    
    slope1 = (y2 - y1) * (x3 - x2)
    slope2 = (y3 - y2) * (x2 - x1)

    
    if slope1 == slope2:
        return True
    else:
        return False


x1, y1 = 1, 2
x2, y2 = 2, 3
x3, y3 = 3, 4

if are_points_collinear(x1, y1, x2, y2, x3, y3):
    print("The points lie on a straight line.")
else:
    print("The points do not lie on a straight line.")

