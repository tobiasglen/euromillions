import random
from dataclasses import dataclass, field
import os
import rich
from rich import table, prompt
from rich.console import Console

console = Console()

prizes = {
      (5,2): {"label": "1st prize"},
      (5,1): {"label": "2nd prize"},
      (5,0): {"label": "3rd prize"},
      (4,2): {"label": "4rd prize"},
      (4,1): {"label": "5th prize"},
      (3,2): {"label": "6th prize"},
      (4,0): {"label": "7th prize"},
      (2,2): {"label": "8th prize"},
      (3,1): {"label": "9th prize"},
      (3,0): {"label": "10th prize"},
      (1,2): {"label": "11th prize"},
      (2,1): {"label": "12th prize"},
      (2,0): {"label": "13th prize"},
    }

class Ticket:
    def __init__(self, generate_winning_numbers=True):
        self.bet_numbers = []
        self.bet_stars = []
        self.winning_numbers = []
        self.winning_stars = []
        # Generate the winning numbers when the ticket is created (default)
        if generate_winning_numbers:
            self.generate_winning_numbers()


    def generate_winning_numbers(self, force_win=False):
        # This method will generate the winning numbers
        # If force_win is True then it will set the winning numbers to one of the bet numbers otherwise it will generate random numbers
        if force_win:
            # Set the winning numbers to one of the bet numbers
            self.winning_numbers = self.bet_numbers[0]
            self.winning_stars = self.bet_stars[0]
        else:
            # Generate the winning numbers
            while len(self.winning_numbers) < 5:
                temp_number = random.randint(1, 50)
                if temp_number not in self.winning_numbers:
                    self.winning_numbers.append(temp_number)

            while len(self.winning_stars) < 2:
                temp_star = random.randint(1, 12)
                if temp_star not in self.winning_stars:
                    self.winning_stars.append(temp_star)

    def check_if_user_won(self):
        # TODO: not sure how this is calculated
        return None
        
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
        if int(bet_star) < 1 or int(bet_star) > 12:
            raise ValueError("Bet star must be between 1 and 12")
        self.bet_stars.append(bet_star)

    def auto_generate_bet(self):
        # This method will generate 5 unique random numbers between 1 and 50 and append them to the bet_numbers list

        # Since a ticket can have multiple bets we can generate a number between 1 and 5 for the number of bets
        number_of_bets = random.randint(2, 5)

        for _ in range(number_of_bets):
            # Generate the bet numbers
            temp_bet_array = []
            while len(temp_bet_array) < 5:
                temp_bet = random.randint(1, 50)
                if temp_bet not in temp_bet_array:
                    temp_bet_array.append(temp_bet)

            self.bet_numbers.append(temp_bet_array)

            # Generate the bet stars
            temp_star_array = []
            while len(temp_star_array) < 2:
                temp_star = random.randint(1, 12)
                if temp_star not in temp_star_array:
                    temp_star_array.append(temp_star)

            self.bet_stars.append(temp_star_array)

    def get_bet_numbers(self):
        return self.bet_numbers

    def get_bet_stars(self):
        return self.bet_stars

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


        if option == 1:
            clear_screen()

            ticket = Ticket(generate_winning_numbers=True)
            if prompt.Confirm.ask("Do you want to auto-generate a random ticket?", default=True):
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
                console.print("Enter stars below:", style="bold yellow")
                while len(ticket.get_bet_stars()) < 2:
                    bet_starr = prompt.Prompt.ask(f"Enter star {len(ticket.get_bet_stars()) + 1}")
                    try:
                        ticket.insert_bet_stars(bet_starr)
                    except ValueError as e:
                        console.print(e, style="bold red")
                        continue

            console.rule("Your Bets", style="bold yellow")

            bets_table = table.Table(show_header=True, header_style="bold magenta")
            bets_table.add_column("Bet", justify="center")
            bets_table.add_column("Numbers", justify="left")
            bets_table.add_column("Stars", justify="left")

            # Get the bet numbers and stars
            bet_numbers = ticket.get_bet_numbers()
            bet_stars = ticket.get_bet_stars()
            print(bet_numbers)
            print(bet_stars)
            # Loop through the bet numbers and stars and print them
            for i in range(len(bet_numbers)):
                bets_table.add_row(str(i + 1), str(bet_numbers[i]), str(bet_stars[i]))

            console.print(bets_table)
            console.line()

            # Print the winning numbers
            if prompt.Confirm.ask("Do you want to \"force a win\" (Set winning numbers to existing bet)?", default=False):
                ticket.generate_winning_numbers(force_win=True)
            console.print(f"Winning Numbers: {ticket.winning_numbers}", style="bold yellow")
            console.print(f"Winning Stars: {ticket.winning_stars}", style="bold yellow")


        elif option == 2:
            ticket.check_if_user_won()
            console.print("Exiting...", style="bold red")
            exit()