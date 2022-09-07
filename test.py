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
        self.winning_numbers,self.winning_stars=generate_valid_numbers()


@dataclass
class Bet:
    bet_numbers: list[int] = field(default_factory=list)
    bet_stars: list[int]  = field(default_factory=list)
    
    def auto_generate_bet(self):
        self.bet_numbers,self.bet_stars=generate_valid_numbers()
    



@dataclass
class Ticket:
    bets: list[Bet] = field(default_factory=list) 

def generate_valid_numbers():
    numbers = []
    stars = []
    while len(numbers) < 5:
        temp_bet = random.randint(1, 50)
        if temp_bet not in numbers:
            numbers.append(temp_bet)
    while len(stars) < 2:
        temp_star = random.randint(1, 12)
        if temp_star not in stars:
            stars.append(temp_star)
    return numbers,stars




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

def check_ticket_bets(ticket):
    bet_numbers = 0
    bet_stars = 0
    for index,bet in enumerate(ticket.bets):
        bet_numbers = bet.bet_numbers
        bet_stars = bet.bet_stars

#A prize consists how many numbers and stars are common to the
#Game winning key.(5,2) -> "1st prize", that means all numbers and stars
#are in a winning bet.
#A Ticket can consist of 1 to multiple winning bets.

def check_if_user_won(ticket,game):
    winning_numbers=game.winning_numbers
    winning_stars=game.winning_stars
    bet_numbers = 0
    bet_stars = 0
    for index,bet in enumerate(ticket.bets):
        bet_numbers = bet.bet_numbers
        bet_stars = bet.bet_stars
        result1 = set(bet_numbers) & set(winning_numbers)
        result2 = set(bet_stars) & set(winning_stars)
        result1_len = len(result1)
        result2_len = len(result2)
        if (result1_len,result2_len) in prizes:
            p=prizes[(result1_len,result2_len)]
            return (f'{p["label"]}')
        else:
            return (f"YOU LOST!")

def play_game():
    game=Game()
    game.generate_winning_numbers()
    while True:
        tickets_menu()
        option = int(prompt.Prompt.ask("Select an option", choices=[str(key) for key in menu_tickets.keys()]))
        if option == 1:
            ticket=Ticket()
            if prompt.Confirm.ask("Do you want to auto-generate a random ticket?", default=True):
                    num_bets = prompt.Prompt.ask(f"Enter number of bets")
                    for _ in range(int(num_bets)):
                        new_bet=Bet()
                        new_bet.auto_generate_bet()
                        ticket.bets.append(new_bet)
                    
                    console.rule("Your Bets", style="bold yellow")

                    bets_table = table.Table(show_header=True, header_style="bold magenta")
                    bets_table.add_column("Bet", justify="center")
                    bets_table.add_column("Numbers", justify="left")
                    bets_table.add_column("Stars", justify="left")

            
                    for i in range(int(num_bets)):
                        tickets_numbers='  '.join(str(x).ljust(3) for x in ticket.bets[i].bet_numbers)
                        tickets_stars='  '.join(str(x).ljust(3) for x in ticket.bets[i].bet_stars)
                        bets_table.add_row(str(i + 1), tickets_numbers,tickets_stars)

                    console.print(bets_table)
                    console.line()
        
        #elif option == 2:  
        #    return
        elif option == 2:
            #exit()
            console.print(check_if_user_won(ticket,game))
            #for i,v in enumerate(ticket.bets):
            #    print(v.bet_numbers)
            #console.print(ticket)
if __name__ == '__main__':
    while True:
        principal_menu()
        option = int(prompt.Prompt.ask("Select an option", choices=[str(key) for key in menu_principal.keys()]))
        if option == 1:
            play_game()
        
        #        tickets=int(prompt.Prompt.ask("Select an option", choices=[str(key) for key in menu_tickets.keys()]))
        #        ticket=Ticket()
        #        
        #elif option == 2:
            #console.print(game)
        elif option == 2:
            exit()

#bets=Bet()
#bets.winning_numbers()
#ticket=Ticket()
#ticket.Bets.append(bets)
#print(ticket.Bets)