from dataclasses import dataclass, field
import random
import os
import rich
from rich import table, prompt
from rich.console import Console
from typing import Optional, List

console = Console()

@dataclass
class Tickets:
    Ticket: list[Ticket] = field(default_factory=list)
    def __post_init__(self):
        return Ticket
@dataclass
class Bet:
    bet_numbers: list[int] = field(default_factory=list)
    bet_stars: list[int]  = field(default_factory=list)
    winning_numbers: list[int] = field(default_factory=list)
    winning_stars: list[int]  = field(default_factory=list)

@dataclass
class Ticket:
    Bets: list[Bet] = field(default_factory=list)
    def __post_init__(self):
        return Bet
   
initial_menu = {1: ['Criar Tickets','Um ou mais Tickets'], 2: ['Sair','Sair do Programa']}


def clear_screen():
    if os.name == 'posix':
        _ = os.system('clear')
    else:
        _ = os.system('cls')

def print_menu():
    menu_table = table.Table(show_header=True, header_style="bold magenta", title="Menu")
    menu_table.add_column("Aposta", justify="center")
    menu_table.add_column("Opções", justify="left")
    menu_table.add_column("Descrições", justify="left")
    for key, value in initial_menu.items():
        menu_table.add_row(str(key), value[0],value[1] )
    console.print(menu_table)

if __name__ == '__main__':
    while True:
        print_menu()
        break
