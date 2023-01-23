#Nous avons utilisé un code prit à cet URL pour réaliser nos tests : https://github.com/adrianeyre/codewars/blob/master/Python/Beta/Bowling.py
#Groupe : Anthony PIGUET ; Lucas DREMAUX
def bowlingScore(frames):
    frame = frames.split(" ")
    score = [[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0],[0,0,0,0,0]]
    finalScore = 0
    frame[9]+="0"
    for i in range(0,3):
        score[9][i] = checkValue(frame[9][i])
        if score[9][i]=="/": score[9][i] = addSpare(score[9][i-1])
    for i in range(8,-1,-1):
        score[i][0] = checkValue(frame[i][0])
        if len(frame[i])!= 1:
            score[i][1] = checkValue(frame[i][1])
        else:
            score[i][1] = None
        if score[i][1]=="/": score[i][1] = addSpare(score[i][0])
    for i in range(0,3):
        if frame[9][i]=="X": finalScore+=10
        if frame[9][i]=="/": finalScore+=int(score[9][i])
        if frame[9][i]!="X" and frame[9][i]!="/": finalScore+=int(score[9][i])
    for i in range(8,-1,-1):
        if frame[i][0]=="X":
            finalScore+=10+score[i+1][0]
            if score[i+1][1]==None:
                finalScore+=score[i+2][0]
            else:
                finalScore+=score[i+1][1]
        else:
            if frame[i][1]=="/":
                finalScore+=10+score[i+1][0]
            else:
                finalScore+=score[i][0]+score[i][1]
    return finalScore

#ajout d'eventuelles cas d'erreurs
def checkValue(pin):
    if pin == "X": return 10
    elif pin == "/": return "/"
    elif int(pin) > 9 or int(pin) < 0:
        return "error"
    return int(pin)

#ajout d'eventuelles cas d'erreurs
def addSpare(pin):
    if int(pin) > 10 or int(pin) < 0:
        return "error"
    return 10 - int(pin)

import random

for rtest in range(0,1):
    xframe = []
    for pinchoice in range(0,9):
        xpin1 = random.randint(0,10)
        if xpin1 != 10:
            xpin2 = random.randint(0,10-xpin1)
            if xpin1 + xpin2 == 10:
                xframe.append(str(xpin1)+"/")
            else:
                xframe.append(str(xpin1)+str(xpin2))
        else:
            xframe.append("X")
    xendframe = ["XXX","12","1/X","34","53","XX1"]
    xframe.append(xendframe[random.randint(0,len(xendframe)-1)])
    xframe = " ".join(xframe)
    
    print("suivie de la partie : ", xframe)
    print("calcul du score final : ",bowlingScore(xframe) )
    
    

        

        