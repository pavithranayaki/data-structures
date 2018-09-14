class NonIntegerError(Exception):
    def int_excep(self):
        print("ENTER INT VALUE")
def dup(list1):
    list2=[]
    try:
        for i in list1:
            if i.isdigit()==0:
                raise NonIntegerError
    except NonIntegerError as er1:
                er1.int_excep()
                
    else:
        for i in list1:
            if i in list2:
                continue
            else:
                list2.append(i)
        print(list2)
list1=[]
n=int(input("ENTER THE RANGE OF LIST1:"))
for i in range(n):
    list1.append(input())
dup(list1)
