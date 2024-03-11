import random

def random_generator():
    return random.randint(1, 10)

print("-------------------------------")
print("   Welcome to the lucky draw")
print("-------------------------------")

guess_chance = 3
# flag initialized
flag = 0

while(guess_chance>0):

    number = int(input("Guess any number between 1 to 10 : "))

    if number == random_generator():
        flag = 1
        break
    else:
        print("\nWrong Guess!!")

    guess_chance -= 1

if __name__ == "__main__":
    if flag == 1:
        print("\nCongrats! You are lucky winner\n")
    else:
        print("\nBetter luck number\n")



