import random


def main():
    level = get_level()
    score =simulate_game(level)
    print("Score: ",score)


def get_level():
    while True:
        try:
            level = int(input("Level: "))
            if level in [1,2,3]:
                break
            else:
                level = input("Level: ")
        except:
            level = input("Level: ")
            pass
    return level

def generate_integer(level):
    if level ==1:
        X = random.randint(0, 9)
        Y = random.randint(0, 9)
    elif level ==2:
        X = random.randint(10,99)
        Y = random.randint(10,99)
    else:
        X = random.randint(100,999)
        Y = random.randint(100,999)
    return X,Y

def simulate(X,Y):
    count =1
    while count <= 3:
        try:
            answer = int(input(f"{X} + {Y} = "))
            if answer == (X + Y):
                return True
            else:
                count +=1
                print("EEE")
        except:
            count +=1
            print("EEE")
    print(f"{X} + {Y} = {X+Y}")
    return False

def simulate_game(level):
    count =1
    score =0
    while count <=10:
        X,Y =generate_integer(level)
        response = simulate(X,Y)
        if response == True:
            score +=1
        count +=1
    return score

if __name__ == "__main__":
    main()
