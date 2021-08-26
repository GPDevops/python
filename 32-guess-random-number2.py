#Computer guess a random number generated by the function "random"
#random.randint(a, b)
#Retorna un entero aleatorio N tal que a <= N <= b. Alias de randrange(a, b+1).
import random

def computer_guess(x):
    low = 1
    high = x
    feedback =""
    while feedback != "c":
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low  #could also be high b/c low = high
        feedback = input(f"Is {guess} to high (H), too low (L) or correct (C)?? ").lower()
        if feedback == "h":
            high = guess - 1
        elif feedback == "l":
            low = guess + 1        
    print(f"Yeah. the computer guessed the number: {guess} correctly")

computer_guess(1000)