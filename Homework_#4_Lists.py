myUniqueList=[]
myLeftovers=[]
def fun(number):
    if number in myUniqueList:
        print("False")
        myLeftovers.append(number)
    else:
        print("True")
        myUniqueList.append(number)

fun(6)
fun(76)
fun(6)
print(myUniqueList)
print(myLeftovers)