''''
1 for rock
2 for scissor
3 for paper
'''
print("Enter 's' for scissor 'r' for rock and 'p' for paper")
import random
computer = random.choice([1 , 2 , 3])
urstr=input("Enter ur choice:")
dict={"r":1 , "s":2 , "p":3}
revdict={1:"Rock" , 2:"Scissor" , 3:"Paper"}
urnum=dict[urstr]
print(f"You chose {revdict[urnum]}\nComputer chose {revdict[computer]}")
if(computer==urnum):
    print("It's a draw!")
else:
    if(computer==1 and urnum==2):
        print("You lose!")
    elif(computer==1 and urnum==3):
        print("You Win!")
    elif(computer==2 and urnum==1):
        print("You Win!")
    elif(computer==2 and urnum==3):
      print("You lose!")
    elif(computer==3 and urnum==1):
      print("You lose!")
    elif(computer==3 and urnum==2):
     print("You Win!")
    else:
        print("something Went wrong!")
    
    

    










