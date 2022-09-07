import random
from dataclasses import dataclass, field
import os
import rich
from rich import table, prompt
from rich.console import Console

console = Console()


def validate_bet_numbers(try_bet_number, temp_bet_dict):
    # Perform validation on the bet numbers
    # It must be an integer between 1 and 50 and must be unique
    if not try_bet_number.isdigit():
        raise ValueError("Bet number must be an integer")
    if try_bet_number in temp_bet_dict["bet_numbers"]:
        raise ValueError("Bet number already exists")
    if int(try_bet_number) < 1 or int(try_bet_number) > 50:
        raise ValueError("Bet number must be between 1 and 50")
    temp_bet_dict["bet_numbers"].append(try_bet_number)
    return temp_bet_dict


def validate_bet_stars(try_bet_star, temp_bet_dict):
    # Perform validation on the bet stars
    # It must be between 1 and 12 and must be unique
    if not try_bet_star.isdigit():
        raise ValueError("Bet star must be an integer")
    if try_bet_star in temp_bet_dict["bet_stars"]:
        raise ValueError("Bet star already exists")
    if int(try_bet_star) < 1 or int(try_bet_star) > 12:
        raise ValueError("Bet star must be between 1 and 12")
    temp_bet_dict["bet_stars"].append(try_bet_star)
    return temp_bet_dict


class Ticket:
    def __init__(self, generate_winning_numbers=True, number_of_bets=1):
        self.bet_numbers = []
        self.bet_stars = []
        self.winning_numbers = []
        self.winning_stars = []
        self.number_of_bets = number_of_bets
        # Generate the winning numbers when the ticket is created (default)
        if generate_winning_numbers:
            self.generate_winning_numbers()

        self.all_bets = []


    def generate_winning_numbers(self, force_win=False):
        # This method will generate the winning numbers
        # If force_win is True then it will set the winning numbers to one of the bet numbers otherwise it will generate random numbers
        if force_win:
            # Set the winning numbers to one of the bet numbers
            self.winning_numbers = self.all_bets[0]["bet_numbers"]
            self.winning_stars = self.all_bets[0]["bet_stars"]
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

    def auto_generate_bet(self):
        # This method will generate 5 unique random numbers between 1 and 50 and append them to the bet_numbers list
        # Since a ticket can have multiple bets we can generate a number between 1 and 5 for the number of bets
        self.number_of_bets = random.randint(2, 5)

        for _ in range(self.number_of_bets):
            temp_bet_dict = {
                "bet_numbers": [],
                "bet_stars": []
            }

            while len(temp_bet_dict["bet_numbers"]) < 5:
                temp_number = random.randint(1, 50)
                if temp_number not in temp_bet_dict["bet_numbers"]:
                    temp_bet_dict["bet_numbers"].append(temp_number)

            while len(temp_bet_dict["bet_stars"]) < 2:
                temp_star = random.randint(1, 12)
                if temp_star not in temp_bet_dict["bet_stars"]:
                    temp_bet_dict["bet_stars"].append(temp_star)

            self.all_bets.append(temp_bet_dict)

    def get_all_bets(self):
        return self.all_bets

    def set_number_of_bets(self, number_of_bets):
        self.number_of_bets = number_of_bets

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
                # Ask the user for how many bets they want to make
                if prompt.Confirm.ask("Do you want to make more than 1 bet?", default=False):
                    number_of_bets = int(prompt.Prompt.ask("How many bets do you want to make?", choices=[str(i) for i in range(1, 6)]))
                    ticket.set_number_of_bets(number_of_bets)

                for _ in range(ticket.number_of_bets):
                    temp_bet_dict = {
                        "bet_numbers": [],
                        "bet_stars": []
                    }
                    # Manually prompt the user to enter the numbers
                    console.print("Enter bet numbers below:", style="bold yellow")
                    while len(temp_bet_dict["bet_numbers"]) < 5:
                        bet_number = prompt.Prompt.ask(f"Enter number {len(temp_bet_dict['bet_numbers']) + 1}")
                        try:
                            temp_bet_dict = validate_bet_numbers(bet_number, temp_bet_dict)
                        except ValueError as e:
                            console.print(e, style="bold red")
                            continue

                    # Now prompt the user to enter the stars
                    console.print("\nEnter bet stars below:", style="bold yellow")
                    while len(temp_bet_dict["bet_stars"]) < 2:
                        bet_star = prompt.Prompt.ask(f"Enter star {len(temp_bet_dict['bet_stars']) + 1}")
                        try:
                            temp_bet_dict = validate_bet_stars(bet_star, temp_bet_dict)
                        except ValueError as e:
                            console.print(e, style="bold red")
                            continue

                    ticket.all_bets.append(temp_bet_dict)




            console.rule("Your Bets", style="bold yellow")

            bets_table = table.Table(show_header=True, header_style="bold magenta")
            bets_table.add_column("Bet", justify="center")
            bets_table.add_column("Numbers", justify="left")
            bets_table.add_column("Stars", justify="left")

            # Get the bet numbers and stars
            all_bets = ticket.get_all_bets()

            # Loop through the bet numbers and stars and print them
            for i in range(len(all_bets)):
                bets_table.add_row(str(i + 1), str(all_bets[i]['bet_numbers']), str(all_bets[i]['bet_stars']))

            console.print(bets_table)
            console.line()

            # Print the winning numbers
            if prompt.Confirm.ask("Do you want to \"force a win\" (Set winning numbers to existing bet)?", default=False):
                ticket.generate_winning_numbers(force_win=True)
            console.print(f"Winning Numbers: {ticket.winning_numbers}", style="bold yellow")
            console.print(f"Winning Stars: {ticket.winning_stars}", style="bold yellow")


        elif option == 2:
            console.print("Exiting...", style="bold red")
            exit()
