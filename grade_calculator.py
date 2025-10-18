def calculate_grade(x):
    if x==100 or x>=90:
        return "A"
    elif x==89 or x>=80:
        return "B"
    elif x==79 or x>=70:
        return "C"
    elif x==69 or x>=60:
        return "D"
    elif x==59 or x>=50:
        return "F"
    elif x>100 or x<1:
        raise ValueError("Not a Vaild Number ")
    return x

    
