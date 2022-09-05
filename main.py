from dataclasses import dataclass, field
import os


@dataclass
class Bet:
    numbers: list[int] = field(default_factory=list)
    stars: list[int] = field(default_factory=list)


@dataclass
class Ticket:
    Bets: list[Bet] = field(default_factory=list)

    def __post__init(self):
        return Bet


options_menu = {1: 'Enter User Keys',
                2: 'Option2',
                3: 'Exit'}


def print_menu():
    for key in options_menu.keys():
        print(key, "---", options_menu[key])


def get_user_numbers():
    numbers = []
    luckystars = []
    print('Enter numbers: ')
    number = input()
    while True:
        while not number.isdecimal():
            number = input('Number not between 1 and 51 try again: ')
        num = int(number)
        if 0 < num < 51:
            if num in numbers:
                number = input(f"{num} already there try again: ")
            else:
                number = input('Enter next number: ')
                numbers.append(num)
        if len(numbers) == 5:
            break
    print('Enter stars: ')
    stars = input()
    while True:
        while not stars.isdecimal():
            stars = input('Number not between 1 and 51 try again: ')
        star = int(stars)
        if 0 < star < 13:
            if star in luckystars:
                stars = input(f"{star} already there try again: ")
            else:
                stars = input('Enter next number: ')
                luckystars.append(star)
        if len(luckystars) == 2:
            break
    return Bet(numbers, luckystars)


def insert_number_ticket(ticket):
    bets = get_user_numbers()
    ticket.Bets.append(bets)
    print(f'Aposta {bets.numbers} {bets.stars}')


def display_bets():
    print(Bet.numbers, Bet.stars)


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def print_menu():
    for key in options_menu.keys():
        print(key, "---", options_menu[key])


if __name__ == '__main__':
    ticket = Ticket()
    while True:
        print_menu()
        option = None
        while option not in options_menu.keys():
            try:
                option = int(input('Select option: '))
                if option not in options_menu.keys():
                    print(f'Enter a number between 1 and {len(options_menu)}')
            except ValueError:
                print('Invalid option')

        match option:
            case 1:
                clear_screen()
                insert_number_ticket(ticket)
                option = int(input('Want to insert another ticket?: '))
                if option != 1:
                    exit()
                elif option == 1:
                    clear_screen()
                    insert_number_ticket(ticket)
            case 2:
                clear_screen()
                insert_number_ticket(ticket)

            case 3:
                exit()
