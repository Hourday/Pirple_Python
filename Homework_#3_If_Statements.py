def fun(a,b,c):
    if a == b :
        print("True")
    elif b == c:
        print("True")
    elif a == c:
        print("True")
    elif a==b and b==c:
        print("True")
    elif a == b and a == c:
            print("True")
    elif b == c and a == c:
        print("True")
    elif a == b and b == c and a == c:
        print("True")
    else:
        print("False")
fun (2,2,3)