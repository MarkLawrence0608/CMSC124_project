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
    
    def parser(self, line):
        keywords = {
            "START": r"^HAI$",
            "END": r"^KTHXBYE$",
            "WAZZUP": r"^WAZZUP$",
            "BUHBYE": r"^BUHBYE$",
            "BTW": r"^BTW.*$",
            "OBTW": r"^OBTW.*$",
            "TLDR": r"^TLDR$",
            "I HAS A": r"^I HAS A$",
            "ITZ": r"^ITZ$",
            "R": r"^R$",
            "SUM OF": r"^SUM OF$",
            "DIFF OF": r"^DIFF OF$",
            "PRODUKT OF": r"^PRODUKT OF$",
            "QUOSHUNT OF": r"^QUOSHUNT OF$",
            "MOD OF": r"^MOD OF$",
            "BIGGR OF": r"^BIGGR OF$",
            "SMALLR OF": r"^SMALLR OF$",
            "BOTH OF": r"^BOTH OF$",
            "EITHER OF": r"^EITHER OF$",
            "WON OF": r"^WON OF$",
            "NOT": r"^NOT$",
            "ANY OF": r"^ANY OF$",
            "ALL OF": r"^ALL OF$",
            "BOTH SAEM": r"^BOTH SAEM$",
            "DIFFRINT": r"^DIFFRINT$",
            "SMOOSH": r"^SMOOSH$",
            "MAEK": r"^MAEK$",
            "A": r"^A$",
            "IS NOW A": r"^IS NOW A$",
            "VISIBLE": r"^VISIBLE$",
            "GIMMEH": r"^GIMMEH$",
            "O RLY?": r"^O RLY\?$",
            "YA RLY": r"^YA RLY$",
            "MEBBE": r"^MEBBE$",
            "NO WAI": r"^NO WAI$",
            "OIC": r"^OIC$",
            "WTF?": r"^WTF\?$",
            "OMG": r"^OMG$",
            "OMGWTF": r"^OMGWTF$",
            "IM IN YR": r"^IM IN YR$",
            "UPPIN": r"^UPPIN$",
            "NERFIN": r"^NERFIN$",
            "YR": r"^YR$",
            "TIL": r"^TIL$",
            "WILE": r"^WILE$",
            "IM OUTTA YR": r"^IM OUTTA YR$",
            "HOW IZ I": r"^HOW IZ I$",
            "IF U SAY SO": r"^IF U SAY SO$",
            "GTFO": r"^GTFO$",
            "FOUND YR": r"^FOUND YR$",
            "I IZ": r"^I IZ$",
            "MKAY": r"^MKAY$",
        }
        # ============== Match keywords condition ==============   


    def mainloop(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                pass
                

root = tk.Tk()
app = Interpreter(root)
root.mainloop()