import random
import pyfiglet


banner = pyfiglet.figlet_format("Rock  Paper  Scissor  Game")
print(banner)
print('''Rules:
Rock can beat Scissor
Scissor can beat Paper
Paper can beat Rock''')

while True: 
    n = 0
    while not n:
        try:
            n = int(input("Enter your Choice | Rock - 1 | Paper - 2 | Scissor - 3 | "))
            if n not in (1,2,3):
                raise ValueError
        except ValueError:
            n = 0
            print("That's not a valid option.")

    comp = random.randint(1,4)

    if n == comp:
        print(pyfiglet.figlet_format("Draw"))

    elif (n == 1 and comp == 2) or (n == 2 and comp == 3) or (n == 3 and comp == 1):
        print(pyfiglet.figlet_format("You  Lose"))      

    elif (n == 1 and comp == 3) or (n == 2 and comp == 1) or (n == 3 and comp == 2):  
        print(pyfiglet.figlet_format("You  Won"))

    print('''Thankyou For playing
    press any key to continue
    3or to quit type exit''') 
    m = input()  
    if m == "exit":
        break     
