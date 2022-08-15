import tkinter as tk
from typing import List

class Calculator:
    def __init__(
            self,
            root: tk.Tk,
            label: tk.Label,
            display: tk.Entry,
            button: List[List[tk.Button]]
    ):
        self.root = root
        self.label = label
        self.display = display
        self.button = button