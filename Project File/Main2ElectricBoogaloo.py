#idfk know what to call this section but its all my variables and shit that wont be called normal
from itertools import repeat
from operator import truediv
from tabnanny import check
import random
Decksecks = []
UserCards = []
CardValue = 0
CardsAmount = 0
Start = True
End = False
Lose = False
Win = False
#Ill add more if i need too

#This part like adds the starting cards for the user
for i in range (1,14):
    for j in range (4):
        if i == 11:
            Decksecks.append("J");
        elif i == 12:
            Decksecks.append("Q");
        elif i == 13:
            Decksecks.append("K");
        elif i == 1:
            Decksecks.append("A");
        else:
            Decksecks.append(i);

def Start_Game():
    Value = []
    return Value

def Card_Generation():
    Value = []
    Value.append(random.randint(1,13))
    return Value




while Start == True:
    input("...")
    if "hit":
       CardValue = Card_Generation()
       UserCards.append(CardValue)
    if "testdecksecks":
        print(Decksecks)
    else:
       Start = False




