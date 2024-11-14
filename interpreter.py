import re
import tkinter as tk
from tkinter import filedialog
from pathlib import Path
'''
Create Parser
Create Dictionary for RegEx
Identify SUM DIFF PRODUKT QUOSHUNT
SPACING
VARIABLES
'''
class Interpreter:
    def __init__(self, root):
        self.root = root
        self.root.title("")
        self.file_path = filedialog.askopenfilename(title="Select a file")
        self.variables = {}
        self.comment_block = False
        self.gui_widgets()
                
    def gui_widgets(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='white', borderwidth=0, highlightthickness=0, relief=tk.SOLID)
        self.canvas.pack(side=tk.TOP, padx=(2,0), pady=(2,0))
        self.mainloop()

    def mainloop(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                print(line)

root = tk.Tk()
app = Interpreter(root)
root.mainloop()