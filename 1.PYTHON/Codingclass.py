class Queries():
    def subFields():
        Lists=["Machine Learning","Neural Networks","Vision","Robotics","Speech Processing","Natural Language Processing"]
        print("subfields in AI are: ")
        for AI_lists in Lists:
            print(AI_lists)
              #  subFields()
    def Odd_or_Even(): 
        user_number=int(input("enter a number :"))
        if(user_number%2==0):
            print(user_number,"is Even number")
            text="Even Number"
        else:
            print(user_number, "is Odd number")
            text="Odd number"
        return(text)    
        Odd_or_Even()            
    def Eligible():
        Gender=input("Your Gender: ")
        print("Your Gender:", Gender)
        Age=int(input("Your Age:"))
        print("Your Age:", Age)
        if(Gender=="Female"and Age>=18 or Gender=="Male" and Age>=21):
            print("ELIGIBLE")
            message="ELIGIBE"
        else:
            print("NOT ELIGIBLE")
            message="NOT ELIGIBLE"
        return (message) 
        Eligible()  
    def percentage():
        English=int(input("Subject1="))
        Tamil=int(input("Subject2="))
        Maths=int(input("Subject3="))
        Science=int(input("Subject4="))
        Social=int(input("Subject5="))
        Total=English+Tamil+Maths+Science+Social
        percentage=Total/500*100
        print("Total =",Total)
        print("Percentage =", percentage)
        per=percentage
        return per
        percentage()
    def triangle():
        h=int(input("Height:"))
        b=int(input("Breadth:"))
        Area=h*b/2
        print("Area of Triangle:",Area)
        H1=int(input("Height1:"))
        H2=int(input("Height2:")) 
        Br=int(input("breadth:"))
        Total=H1+H2+Br
        print("Perimeter of triangle:",Total)
           
