for rows in range(5):
    if rows%2==0: #0,2,4
        for columns in range(1,6,1):
            if columns%2==1:
                if columns!=5:
                    print(" ",end="")
                else:
                    print(" ")
            else:
                print("|", end="")
    else: #1,3
        print("-----")