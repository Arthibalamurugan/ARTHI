mark =int(input("enter mark: "))
if mark < 0 or mark>100:
    print("invalid mark")
elif mark >=90:
    print("A")
elif mark >=70:
    print("B")
elif mark >=50:
    print("C")
elif mark >=40:
    print("D")
else:
    print("Fail")