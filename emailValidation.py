email=input("enter your email")   
# g@g.in
j,k=0,0
if len(email)>=6:
    if email[0].isalpha():
        if ('@' in email)and(email.count('@')==1):
            if (email[-3]=='.') ^ (email[-4]=='.'):
                for i in email:
                    if i==' ' and k==0:
                        k=1
                        print("wrong email6")
                    elif i.isupper() and j==0:
                        
                        print("wrong email7")
                        j=1
                           
                else:
                   print("right email")

            else:
                print("wrong email4")
        else:
            print("wrong email3")
    else:
        print("wrong email2")
else:
    print("wrong email 1")
