A1=int(input("Enter Marks of first Assignment (Less then 100)"))
A2=int(input("Enter Marks of second Assignment (Less then 100)"))
A3=int(input("Enter Marks of third Assignment (Less then 100)"))
E1=int(input("Enter Marks of first Exam (Less then 100)"))
E2=int(input("Enter Marks of Second Exam (Less then 100)"))
weighted_score = ( A1 + A2 + A3 ) *0.1 + (E1 + E2 ) * 0.35
print("Weighted Score -",weighted_score)