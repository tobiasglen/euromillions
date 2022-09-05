import random
from dataclasses import dataclass, field
import os
import rich
from rich import table, prompt
from rich.console import Console

console = Console()



class Ticket:
    def __init__(self):
        self.bet_numbers = []
        self.bet_stars = []

    def insert_bet_numbers(self, bet_number):
        # Perform validation on the bet numbers
        # It must be an integer between 1 and 50 and must be unique
        if not bet_number.isdigit():
            raise ValueError("Bet number must be an integer")
        if bet_number in self.bet_numbers:
            raise ValueError("Bet number already exists")
        if int(bet_number) < 1 or int(bet_number) > 50:
            raise ValueError("Bet number must be between 1 and 50")
        self.bet_numbers.append(bet_number)

    def insert_bet_stars(self, bet_star):
        # Perform validation on the bet stars
        # It must be between 1 and 12 and must be unique
        if bet_star in self.bet_stars:
            raise ValueError("Bet star already exists")
        if bet_star < 1 or bet_star > 12:
            raise ValueError("Bet star must be between 1 and 12")
        self.bet_stars.append(bet_star)

    def auto_generate_bet(self):
        # This method will generate 5 unique random numbers between 1 and 50 and append them to the bet_numbers list
        while len(self.bet_numbers) < 5:
            bet_number = random.randint(1, 50)
            if bet_number not in self.bet_numbers:
                self.bet_numbers.append(bet_number)

        # generate 2 unique random numbers between 1 and 12 and append them to the bet_stars list
        while len(self.bet_stars) < 2:
            bet_star = random.randint(1, 12)
            if bet_star not in self.bet_stars:
                self.bet_stars.append(bet_star)

    def get_bet_numbers(self):
        return self.bet_numbers

    def __str__(self):
        # This is just a helper method to print the ticket. Not really needed
        return f'Numbers: {self.bet_numbers}\nStars: {self.bet_stars}'




initial_menu = {1: 'Make Ticket', 2: 'Exit'}



def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')


def print_menu():
    menu_table = table.Table(show_header=True, header_style="bold magenta", title="Menu")
    menu_table.add_column("ID", justify="center")
    menu_table.add_column("Option", justify="left")
    menu_table.add_column("Description", justify="left")
    for key, value in initial_menu.items():
        menu_table.add_row(str(key), value, "None atm")
    console.print(menu_table)


if __name__ == '__main__':
    while True:
        print_menu()
        option = int(prompt.Prompt.ask("Select an option", choices=[str(key) for key in initial_menu.keys()]))


        match option:
            case 1:
                clear_screen()

                ticket = Ticket()
                if prompt.Confirm.ask("Do you want to auto-generate a random ticket?"):
                    ticket.auto_generate_bet()
                else:
                    # Manually prompt the user to enter the numbers
                    console.print("Enter numbers below:", style="bold yellow")
                    while len(ticket.get_bet_numbers()) < 5:
                        bet_number = prompt.Prompt.ask(f"Enter number {len(ticket.get_bet_numbers()) + 1}")
                        try:
                            ticket.insert_bet_numbers(bet_number)
                        except ValueError as e:
                            console.print(e, style="bold red")
                            continue

                console.print(ticket.bet_numbers)


            case 2:
                console.print("Exiting...", style="bold red")
                exit()
