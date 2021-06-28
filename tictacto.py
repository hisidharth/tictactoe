gameboard=["1","2","3","4","5","6","7","8","9"]
turns=1
p1=input("name, you will be x")
p2=input("name, you will be o")
game=True
def callboard():
    print(gameboard[0:3])
    print(gameboard[3:6])
    print(gameboard[6:9])
callboard()
    
while game==True:
    players="x"
    if turns%2==0:
        players="o"
        game=True
        turns+=1
    else:
        players="x"
        game=True
        turns+=1
    answer=int(input("number?"))-1
    if gameboard[answer]=="x" or gameboard[answer]=="o":
        print("invalid choice")
        callboard()
        game=True
    else:
        gameboard[answer]=players
        callboard()
        game=True
    if gameboard[0]==gameboard[1] and gameboard[1]== gameboard[2]:
        if gameboard[0]=="x":
            print(p1,"wins")
            game=False
        else:
            print(p2,"wins")
            game=False
    elif gameboard[0]==gameboard[4] and gameboard[4]== gameboard[8]:
        if gameboard[0]=="x":
            print(p1,"wins")
            game=False
        else:
            print(p2,"wins")
            game=False
    elif gameboard[0]==gameboard[3] and gameboard[3]==gameboard[6]:
        if gameboard[0]=="x":
            print(p1,"wins")
            game=False
        else:
            print(p2,"wins")
            game=False
    elif gameboard[3]==gameboard[4] and gameboard[4]== gameboard[5]:
        if gameboard[3]=="x":
            print(p1,"wins")
            game=False
        else:
            print(p2,"wins")
            game=False
    elif gameboard[6]==gameboard[7] and gameboard[7]== gameboard[8]:
        if gameboard[6]=="x":
            print(p1,"wins")
            game=False
        else:
            print(p2,"wins")
            game=False
    elif gameboard[1]==gameboard[4] and gameboard[4]== gameboard[7]:
        if gameboard[1]=="x":
            print(p1,"wins")
            game=False
        else:
            print(p2,"wins")
            game=False
    elif gameboard[2]==gameboard[5] and gameboard[5]== gameboard[8]:
        if gameboard[2]=="x":
            print(p1,"wins")
            game=False
        else:
            print(p2,"wins")
            game=False
    elif gameboard[2]==gameboard[4] and gameboard[4]== gameboard[6]:
        if gameboard[2]=="x":
            print(p1,"wins")
            game=False
        else:
            print(p2,"wins")
            game=False
    
        
        
        
    
    
        
