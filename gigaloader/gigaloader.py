# Module imports
from jutl.formatting import apply
import shutil
from time import sleep
from random import random

# External visibility
__all__ = ['GigaLoader']


class GigaLoader(object):
    """
    Class which prints a loading bar
    in the terminal upon execution.
    """
    def __init__(self, name: str = None, length: int = None, num_checkpoints: int = None, print_percentage: bool = False):
        self.name: str = name
        if length is not None:
            self.terminal_width = length
        else:
            self.terminal_width, _ = shutil.get_terminal_size()
            self.terminal_width -= len(self.name) + 4
        self.num_checkpoints: int = num_checkpoints
        self.current_checkpoint: int = 0
        self.progress_percentage: float = 0.0
        self.progress_chars: int = 0
        self.empty_space: int = 0
        self.print_percentage: bool = print_percentage

    def print_terminal_size(self):
        print(f"Terminal size: {self.terminal_width} chars wide.")
    
    def print_update(self):
        print(f"{self.name}: [{apply('=', text_color='yellow') * self.progress_chars}{' ' * self.empty_space}] {int(self.progress_percentage * 100) if self.print_percentage else ''}{'%' if self.print_percentage else ''}", end="\r")
        print(f"{apply('Complete.', text_color='green')}") if self.current_checkpoint == self.num_checkpoints else None

    def increment_checkpoint(self):
        self.current_checkpoint += 1
        self.progress_percentage = self.current_checkpoint / self.num_checkpoints
        self.progress_chars = int(self.terminal_width * self.progress_percentage)
        self.empty_space = int(self.terminal_width - self.progress_chars)
        # print() if self.progress_percentage == 1 else None
        self.print_update()

    def print_separator(self):
        print(f"{'=' * (self.terminal_width)}")
