from dataclasses import dataclass, field, InitVar
from typing import Optional
import random
@dataclass
class Ticket:
    bet_numbers: list[int] = field(default_factory=list)
    bet_stars: list[int]  = field(default_factory=list)
    winning_numbers: list[int] = field(default_factory=list)
    winning_stars: list[int]  = field(default_factory=list)
    def __post__init__(self,generate_winning_numbers=True):
        if generate_winning_numbers:
            generate_winning_numbers()
    def generate_winning_numbers(self):
        return self.bet_stars
