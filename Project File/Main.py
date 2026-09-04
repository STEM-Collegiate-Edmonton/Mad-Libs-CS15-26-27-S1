import random
Dealer_Card1 = (random.randint(1,13))
Dealer_Card2 = (random.randint(1,13))
Card1 = (random.randint(1,13))
Card2 = (random.randint(1,13))
Move = "NA"
score = 0
Dealer_score = 0
Start = True
Game = True


while Start == True:
#Dealer Cards
    if 2 <= Dealer_Card1 <= 10:
        score += Dealer_Card1

    if Dealer_Card1 == 11:
        Dealer_Card1 = "J"
        Dealer_score += 10
    if Dealer_Card1 == 12:
        Dealer_Card1 = "Q"
        Dealer_score += 10
    if Dealer_Card1 == 13:
        Dealer_Card1 = "K"
        Dealer_score += 10
    if Dealer_Card1 == 1 and score >= 21:
        Dealer_Card1 = "A11"
        Dealer_score += 11
    elif score >= 21:
        Dealer_Card1 = "A1"
        Dealer_score += 1

    if 2<= Dealer_Card2 <= 10:
        Dealer_score += Dealer_Card2

    if Dealer_Card2 == 11:
        Dealer_Card2 = "J"
        Dealer_score += 10
    if Dealer_Card2 == 12:
        Dealer_Card2 = "Q"
        Dealer_score += 10
    if Dealer_Card2 == 13:
        Dealer_Card2 = "K"
        Dealer_score += 10
    if Dealer_Card2 == 1 and score >= 21:
        Dealer_Card2 = "A11"
        Dealer_score += 11
    elif score >= 21:
        Dealer_Card2 = "A1"
        Dealer_score += 1

    if 2<= Card1 <= 10:
        Dealer_score += Card1

    if Card1 == 11:
        Card1 = "J"
        score += 10
    if Card1 == 12:
        Card1 = "Q"
        score += 10
    if Card1 == 13:
        Card1 = "K"
        score += 10
    if Card1 == 1 and score >= 21:
        Card1 = "A11"
        score += 11
    elif score > 21:
        Card1 = "A1"
        score += 1


    if 2<= Card2 <= 10:
        score += Card2

    if Card2 == 11:
        Card2 = "J"
        score += 10
    if Card2 == 12:
        Card2 = "Q"
        score += 10
    if Card2 == 13:
        Card2 = "K"
        score += 10
    if Card2 == 1 and score <= 21:
            Card2 = "A11"
            score += 11
    elif score > 21:
            Card2 = "A1"
            score += 1

    if Card1 == "A1" and Card2 == "A1":
            Card1 = "A11"
            score = 12

    print("Dealer Cards")
    print(Dealer_Card1, Dealer_Card2)

    print("Your Cards")
    print(Card1, Card2)

    Start = False

while score <= 21 and Start == False:
    Move = input("Hit or Stand")
    if Move == "Hit" or " Hit":
        Card3 = (random.randint(1,13))
        if 2<= Card3 <= 10:
            score += Card3
        if Card3 == 11:
            Card3 = "J"
            score += 10
        if Card3 == 12:
            Card3 = "J"
            score += 10
        if Card3 == 13:
            Card3 = "J"
            score += 10
        if Card3 == 1:
            Card3 = "A"
            score += 11
        print(Card1, Card2, Card3)
    if Move == "Stand" or " Stand" and score > Dealer_score:
        print("You Win")

print (score)






if score == 21:
    print ("WINNERRRRRRRR")
else:
    print ("Busted:(")









