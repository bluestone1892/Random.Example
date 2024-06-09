import random 

random_number = random.randint(1, 100)

game_count = 1 

while True: 
    try:
        my_number = int(input("1~100사이의 숫자를 입력")) 


        if  my_number > random_number: 
            print("dawn")
        elif my_number < random_number: 
            print("up")
        elif my_number == random_number: 
            print(f"{game_count}회만에 맞춤")
            break
    

        game_count = game_count + 1 
    except:
        print("숫자를 입력하세요")

