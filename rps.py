import random


while True:
    comp = random.choice(["rock", "paper", "scissors"])

    user = input("Welcome to the game.\nPlease choose one: Rock, Paper or Scissors?").lower()

    print(f"Datorn valde {comp} och du valde {user}.")

    # Din uppgift är att koda m.h.a if, elif och else ett program som skriver ut resultatet på spelet
    # rock slår scissors, scissors slår paper, paper slår rock
    # Tips: Använd and/or/nästlade if-satser för att förenkla koden
    # Extra: Lägg till att man spelar till 3 poäng istället för att spela oändligt.

