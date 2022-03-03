import random

celebs = [
    ["Jennifer Anniston", 39_900_000],
    ["Dwayne Johnson", 300_000_000],
    ["Cardi B", 124_000_000],
    ["Tom Cruise", 6_100_000],
    ["Tom Hanks", 9_300_000],
    ["Johnny Depp", 11_800_000],
    ["Leonardo DiCaprio", 52_500_000],
    ["Natalie Portman", 7_500_000],
    ["Jessica Alba", 19_500_000],
    ["Drake", 103_000_000],
    ["Robert Downey Jr", 51_600_000],
    ["Will Smith", 58_400_000],
    ["Angelina Jolie", 12_300_000],
    ["Katy Perry", 153_000_000],
    ["Vin Diesel", 78_400_000],
    ["Justin Bieber", 221_000_000],
    ["Ellen", 115_000_000],
    ["Adele", 49_500_000],
    ["Drew Barrymore", 15_300_000],
    ["Channing Tatum", 16_900_000],
    ["Mark Wahlberg", 18_100_000],
    ["Arnold Schwarzenegger", 22_100_000],
    ["Nicki Minaj", 175_000_000],
    ["Ben Stiller", 1_750_000],
    ["Taylor Swift", 201_000_000],
    ["Selena Gomez", 299_000_000],
    ["Ariana Grande", 296_000_000],
    ["Priyanka Chopra", 74_600_000],
    ["Nick Jonas", 32_200_000],
    ["Beyonce", 240_000_000],
    ["Rihanna", 122_000_000],
    ["Zendaya", 131_000_000],
    ["Tom Holland", 63_400_000],
    ["Barack Obama", 35_300_000],
    ["Michelle Obama", 48_700_000],
    ["Messi", 309_000_000],
    ["Serena Williams", 14_200_000],
    ["Michael Phelps", 3_400_000],
    ["Usain Bolt", 11_200_000],
    ["Tyler The Creator", 12_100_000]
]

gameover = False
score = 0


def getceleb():
    rand = random.randint(0, len(celebs) - 1)
    for _ in range(2):
        return celebs[rand]


def first(getceleb):
    celebA = getceleb
    print(f"A {celebA[0]}")

    return celebA


def second(getceleb):
    celebB = getceleb
    print(f"B {celebB[0]}")

    return celebB


def user_guess(celebA, celebB):
    a_or_b = input("Which celebrity has more followers? A or B: ").lower()
    global score
    global gameover
    if a_or_b == "a":
        if celebA[1] > celebB[1]:
            print("Well Done!")
            score += 1
            print(f"Score: {score}")
            return score
        elif celebA[1] < celebB[1]:
            gameover = True
            print("WRONG:((((: ")
            print(f"Final score: {score}")
            return score
        else:
            print("Same celeb. No points")
            print(f"Score is still {score}")
            return score

    elif a_or_b == "b":
        if celebB[1] > celebA[1]:
            print("Nice job!")
            score += 1
            print(f"Score: {score}")
            return score
        elif celebB[1] < celebA[1]:
            gameover = True
            print("XXXXXX wrong." + str(gameover))
            print(f"Final score: {score}")
            return score
        else:
            print("Same celeb. No points")
            print(f"Score is still {score}")
            return score

    else:
        print("Please enter a or b. Idiot")
        user_guess(celebA, celebB)
        return


def b_2_a(celebA, celebB):
    celebA = celebB
    print(f"A {celebA[0]}")
    return celebA


def new_b(getceleb, celebB):
    celebB = getceleb
    print(f"B {celebB[0]}")
    return celebB


def restart():
    global gameover, score
    r_q = input("\n\n\n\nPress R to play again.  \nPress Q to quit.\n").lower()
    if r_q == "r":
        print("\n\n\n\n")
        score = 0
        gameover = False
        celebA = first(getceleb())
        celebB = second(getceleb())
    elif r_q == "q":
        gameover = True
        return
    else:
        print("Please enter r or q.")
        restart()


celebA = first(getceleb())
celebB = second(getceleb())

while gameover == False:
    score = user_guess(celebA, celebB)
    if gameover is False:
        print("\n\n\n\n\n\n\n\n\n\n\n")
        celebA = b_2_a(celebA, celebB)
        celebB = new_b(getceleb(), celebB)
    elif gameover is True:
        restart()








