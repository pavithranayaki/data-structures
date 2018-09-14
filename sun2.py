class TicketNotAvailableException(Exception):
    def not_av(self):
        print("TICKET IS NOT AVAILABLE")
tic_count=60
rem=0
name=input("ENTER UR NAME:")
n=int(input("NO.OF TICKETS TO BE BOOKED:"))
dic={name:n}
tic_count-=n
rem+=n
while(1):
    print("ENTER UR CHOICE:")
    ch=int(input())
    if ch==1:
        if n>tic_count:
            try:
                raise TicketNotAvailableException
            except TicketNotAvailableException as er1:
                er1.not_av()
    if ch==2:
        if rem>0:
            try:
                raise Exception
            except Exception as er:
                print(er2)
        print(rem)
    
