from dataclasses import dataclass,field
import os
@dataclass
class Bet:
    numbers: list[int] = field(default_factory=list)
    stars: list[int]  = field(default_factory=list)

@dataclass
class Ticket:
    Bets: list[Bet] = field(default_factory=list)
    def __post__init(self):
        return Bet

options_menu = {1:'Enter User Keys',
                2:'Option2',
                3:'Exit'}   

def print_menu():
    for key in options_menu.keys():
        print(key,"---",options_menu[key])

def get_user_numbers():
    numbers = []
    luckystars = []
    print('Enter numbers: ')
    while len(numbers) != 5:
        number=input().strip()
        for num in number:
            if num.isdigit():
                if num not in numbers:
                    numbers.append(num)
    print('Enter stars: ')
    while len(luckystars) != 2:
        lucky=input().strip()
        for luck in lucky:
            if luck.isdigit():
                if luck not in luckystars:
                    luckystars.append(luck)
    return Bet(numbers,luckystars)

def insert_number_ticket(ticket):
    bets=get_user_numbers()
    ticket.Bets.append(bets)
    print(f'Here\'s numbers={bets.numbers} and stars={bets.stars}')


def clear_screen():

    # It is for MacOS and Linux(here, os.name is 'posix')
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        # It is for Windows platfrom
        _ = os.system('cls')
def print_menu():
    for key in options_menu.keys():
        print(key,"---",options_menu[key])

if __name__=='__main__':
    ticket=Ticket()
    while True:
        print_menu()
        option=''
        try:    
            option=int(input("Enter option: "))
        except:
            option=int(input("Try again: "))
        if option==1:
            clear_screen()
            insert_number_ticket(ticket)
            option=int(input('Want to insert another ticket?: '))
            if option != 1:
                exit()
            elif option == 1:
                clear_screen()
                insert_number_ticket(ticket)
        elif option==2:
            pass
        elif option==3:
            exit()
        else:
            option=int(input('Invalid, enter a number between 1 and 3: '))
