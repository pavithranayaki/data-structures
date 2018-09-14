class DuplicateElementException(Exception):
    def dup(self):
        print("DUPLICATE ELEMENT IS FOUND")
class ElementMatchedException(Exception):
    def match(self):
        print("ELEMENT MATCHED")
list_1=[]
list_2=[]
n=int(input("NUMBR OF ELE IN LIST_1:"))
m=int(input("NUMBR OF ELE IN LIST_2:"))
for i in range(n):
    list_1.append(int(input()))
for i in range(m):
    list_2.append(int(input()))
dup=set(list_1)
dup_1=set(list_2)
l1=len(list_1)
l2=len(list_2)
d1=len(dup)
d2=len(dup_1)
print("ENTER UR CHOICE:")
while(1):
    choice=int(input())
    if choice==1:
        try:
            if l1>d1 or l2>d2:
                raise DuplicateElementException
        except DuplicateElementException as er1:
            er1.dup()
    if choice==2:
        try:
            for i in range(n):
                for j in range(m):
                    if i==j:
                        raise ElementMatchedException
        except ElementMatchedException as er2:
            er2.match()
    if choice==3:
        try:
            for i in range(n):
                res=int(list[i])/int(list[i+1])
                print(int(res))
        except Exception as er3:
            print(er3)
    else:
        break
