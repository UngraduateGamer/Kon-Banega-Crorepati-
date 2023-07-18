from playsound import playsound
import time
print("******WELCOME TO THE KON BANEGA CROREPATI******")
playsound("C:\\Users\\Rahul\\Desktop\\Pythons\\Excercises\\KBC\\Kbc Background.mp3")
questions=[
    ["Grand Central Terminal, Park Avenue, New York is the world's ? ","Beautiful Place","park","Amazon Park","None of the Above",1]
    
    ,["Entomology is the science that studies ?","makes perfect","nothing","rehnde","all of the above",4],
    
    ["Which is the Most Pagal Person in the World ?","Prince","Jatin","om","James",1],
    
    [" What is the Highest rank of the garena Free Fire in the Craftland Mode ?","Heroic","Master","Grandmaster","None of these",4], 
    
    ["who is the father of c language ?","Dennis Ritchie","Bjarne Straustrup","Jeorge Boole","prince",1],
    
    ["which Language is Used to design the Web Designing ?","HTML","CSS","JS","All of these",4],
    
    ["which of the following the not the type of RAM ?","SRAM","MRAM","DRAM","EPROM",2],
    
    ["who is Prime Minister in India ?","Narendra Modi","John Cena","Shakepeir","Juley Watson",1],
    
    ["what is the Highest TRP show in the Sony Sab Channel ?","Tmkoc","cid","none","all",1],
    
    ["what is the Best gamer in the world in Free Fire ?","Raistar","B2K","Gyan Sujan","Rahul_yt",1]]

money=0
seconds=0
levels=[1000,2000,4000,6000,15000,75000,98500,135000,145000,200000]
for i in range(len(levels)):
    qus=questions[i]
    print("\nQuestion for Rs.",levels[i],"in your Computer Screen ")
    print("\nQ",i+1,": ",qus[0])
    print("1.",qus[1],"\t","2.",qus[2]) 
    print("3.",qus[3],"\t","4.",qus[4]) 
    results=int(input("Choose the Option(1-4):"))
      
    if results==qus[-1]:
        print("\n\nCorrect Answer You have won Rs.",levels[i])
        if i==5:
            money=15000
            print("Your Take Home Money is Rs." ,money )
        elif i==8:
            money=13500
            print("Your Take Home Money is Rs." ,money )
        elif i==10:
            money=200000
            print("Your Take Home Money is Rs." ,money )
            
    else:
        print("Wrong Answers ")
        playsound("C:\\Users\\Rahul\\Downloads\\Wrong Answer.mp3")
        break
    
print("Your Take Home Money is Rs.",money)
    
        
