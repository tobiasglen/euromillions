from dataclasses import dataclass, field
import random
import os
import rich
from rich import table, prompt
from rich.console import Console

console = Console()

@dataclass
class Game:
    winning_numbers: list[int] = field(default_factory=list)
    winning_stars: list[int]  = field(default_factory=list)
    
    def generate_winning_numbers(self):
        while len(self.winning_numbers) < 5:
            temp_number = random.randint(1, 50)
            if temp_number not in self.winning_numbers:
                self.winning_numbers.append(temp_number)

        while len(self.winning_stars) < 2:
            temp_star = random.randint(1, 12)
            if temp_star not in self.winning_stars:
                self.winning_stars.append(temp_star)

@dataclass
class Bet:
    bet_numbers: list[int] = field(default_factory=list)
    bet_stars: list[int]  = field(default_factory=list)

    
    def auto_generate_bet(self):

            while len(self.bet_numbers) < 5:
                temp_bet = random.randint(1, 50)
                if temp_bet not in self.bet_numbers:
                    self.bet_numbers.append(temp_bet)

            while len(self.bet_stars) < 2:
                temp_star = random.randint(1, 12)
                if temp_star not in self.bet_stars:
                    self.bet_stars.append(temp_star)
        
    def check_if_user_won(self):
        return None
    
    def get_bet_numbers(self):
        return self.bet_numbers

    
    def get_bet_stars(self):
        return self.bet_stars


@dataclass
class Ticket:
    bets: list[Bet] = field(default_factory=list)



menu_principal = {1: ['Criar Tickets','Um ou mais Tickets'], 2: ['Sair','Sair do Programa']}

menu_tickets = {1: ['Criar Apostas','Uma ou mais Apostas'], 2: ['Sair','Voltar ao inicio']}

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

def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def principal_menu():
    menu_table = table.Table(show_header=True, header_style="bold magenta", title="Menu")
    menu_table.add_column("ID", justify="center")
    menu_table.add_column("Opções", justify="left")
    menu_table.add_column("Descrições", justify="left")
    for key, value in menu_principal.items():
        menu_table.add_row(str(key), value[0],value[1] )
    console.print(menu_table)

def tickets_menu():
    menu_table = table.Table(show_header=True, header_style="bold magenta", title="Menu")
    menu_table.add_column("ID", justify="center")
    menu_table.add_column("Opções", justify="left")
    menu_table.add_column("Descrições", justify="left")
    for key, value in menu_tickets.items():
        menu_table.add_row(str(key), value[0],value[1] )
    console.print(menu_table)

def play_game():
    while True:
        tickets_menu()
        option = int(prompt.Prompt.ask("Select an option", choices=[str(key) for key in menu_tickets.keys()]))
        if option == 1:  # new ticket
            ticket=Ticket()
            if prompt.Confirm.ask("Do you want to auto-generate a random ticket?", default=True):
                    num_bets = prompt.Prompt.ask(f"Enter number of bets")
                    for _ in range(int(num_bets)):
                        new_bet=Bet()
                        ticket.bets.append(new_bet)
            
            console.rule("Your Bets", style="bold yellow")

            bets_table = table.Table(show_header=True, header_style="bold magenta")
            bets_table.add_column("Bet", justify="center")
            bets_table.add_column("Numbers", justify="left")
            bets_table.add_column("Stars", justify="left")

            # Get the bet numbers and stars
            bet_numbers = Bet.get_bet_numbers()
            bet_stars = Bet.get_bet_stars()

            # Loop through the bet numbers and stars and print them
            for i in range(len(bet_numbers)):
                bets_table.add_row(str(i + 1), str(bet_numbers[i]), str(bet_stars[i]))

            console.print(bets_table)
            console.line()

        elif option == 2:  # back to main menu
            return
if __name__ == '__main__':
    while True:
        principal_menu()
        option = int(prompt.Prompt.ask("Select an option", choices=[str(key) for key in menu_principal.keys()]))
        if option == 1:
            play_game()
        
        #        tickets=int(prompt.Prompt.ask("Select an option", choices=[str(key) for key in menu_tickets.keys()]))
        #        ticket=Ticket()
        #        
        
        elif option == 2:
            exit()

#bets=Bet()
#bets.winning_numbers()
#ticket=Ticket()
#ticket.Bets.append(bets)
#print(ticket.Bets)