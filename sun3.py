class MarkNotValidException(Exception):
    def mark_error(self):
        print("ENTER VALID MARK")
class RegisterNumberNotValidException(Exception):
    def regnum_error(self):
        print("ENTER VALID REG_NUM")
print("NUMBER OF TESTCASES:")
n=int(input())
if  n<10:
    for i in range(n):
        mark1=int(input("MARK_1:"))
        mark2=int(input("MARK_2:"))
        mark3=int(input("MARK_3:"))
        reg_no=input("REG_NO:")
        try:
            if mark1>100 or mark2>100 or mark3>100:
                raise MarkNotValidException
        except MarkNotValidException as er1:
            er1.mark_error()
            break
        try:
            if reg_no.isnumeric()==0:
                raise RegisterNumberNotValidException
        except RegisterNumberNotValidException as er2:
            er2.regnum_error()
            break
        name=input("NAME:")
        total=mark1+mark2+mark3
        if 250<total<300:
            print("GRADE IS A")
        elif 200<total<249:
            print("GRADE IS B")
        elif 150<total<199:
            print("GRADE IS C")
        elif 100<total<149:
            print("GRADE IS D")
        else:
            print("GRADE IS E")


    
