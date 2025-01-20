print("Welcome to KBC \U0001F64F")
ready=input("Are you ready? (Yes/No)\n")
if ready.lower()=='yes':
    print("Aapki computer screen par QUESTION Aane wala hai")
else:
    print("Tayyari karke Aaeye")
    
def questions():
    score=0
    
    q1=input("Question No:01\nTaj Mahal kis ne Banaya?\nOPTIONS:\n(a)Akbar (b)Baber (c)Shah Janha (d)Shoeb Alam\n")
    if q1=='c':
        print(" \u2705 Correct Answer")
        score +=1
    else:
        print("\u274C Wrong Answer")   
        
    q2=input("Question No:02\nTesla ka CEO kon hai?\nOPTIONS:\n(a)Elon Musk (b)Mark Zukerberg (c)Bill Gates (d)Shoeb Alam\n")
    if q2=='a':
        print(" \u2705 Correct Answer")
        score +=1
    else:
        print("\u274C Wrong Answer")   
        
    q3=input("Question No:03\nCR7 kaun hai?\nOPTIONS:\n(a)Cricketer (b)Footballer (c)Tennis player (d)Racer\n")
    if q3=='b':
        print(" \u2705 Correct Answer")
        score +=1
    else:
        print("\u274C Wrong Answer")   
        
    q4=input("Question No:04\nWho's the best coder in the world?\nOPTIONS:\n(a)Mark zukerberg (b)Harry (c)ChatGpt (d)Shoeb Alam\n")
    if q4=='d':
        print(" \u2705 Correct Answer")
        score +=1
    else:
        print("\u274C Wrong Answer")  
        
    q5=input("Question No:05\nShoeb Alam kis city se belong karte hai?\nOPTIONS:\n(a)Mumbai (b)Pune (c)Nagpur (d)Begluru\n")
    if q5=='c':
        print(" \u2705 Correct Answer")
        score +=1
    else:
        print("\u274C Wrong Answer")                                    
        
    if score==5:
        print("\U0001F389 Congratulations\n You WIN the 10 CRORE \U0001F4B8  Rupees ")
    else:
        print(f"Your score is {score}/5.Better luck next time!")
        
if ready.lower()=='yes':
        questions()