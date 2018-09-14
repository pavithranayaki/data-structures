class MedicallyUnfitException(Exception):
    def unfit(self):
        print("UNFIT")
n=int(input("NO.OF PEOPLE TO BE TESTED:"))
for i in range(n):
    name=input("ENTER THE NAME:")
    weight=int(input("ENTER THE WEIGHT:"))
    print("CHECKING FOR EYE PROBLEM")
    eye_prob=input("YES / NO\n")
    print("CHECKING FOR COMMUNICABLE DISEASES")
    disease=input("YES / NO\n")
    try:
        if weight<45 or eye_prob=="YES" or disease=="YES":
            raise MedicallyUnfitException
    except MedicallyUnfitException as er1:
        er1.unfit()
    else:
        print("MEDICALLY FIT")
            
        
    
