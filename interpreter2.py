import re
import tkinter as tk
from tkinter import filedialog

class Interpreter:
    def __init__(self, root):
        self.root = root
        self.root.title("LOLCode Interpreter")
        self.file_path = filedialog.askopenfilename(title="Select a file")
        self.variables = {}
        self.comment_block = False
        self.gui_widgets()

    def gui_widgets(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='white', borderwidth=0, highlightthickness=0, relief=tk.SOLID)
        self.canvas.pack(side=tk.TOP, padx=(2, 0), pady=(2, 0))
        self.mainloop()

    def tokenize(self, line):
        token_pattern = r'"[^"]*"|\S+|[+\-*/%=<>&|^!"\'(),.]'  
        tokens = re.findall(token_pattern, line.strip())

        complex_tokens = ['SUM OF', 'PRODUKT OF', 'BIGGR OF', 'DIFF OF', 'QUOSHUNT OF']
        
        for complex_token in complex_tokens:
            line = line.replace(complex_token, complex_token.replace(" ", "_"))
        
        tokens = re.findall(token_pattern, line.strip())

        tokens = [token.replace("_", " ") for token in tokens]
        
        return tokens



    def parser(self, tokens):
        if not tokens:
            return None

        keywords = {
            "HAI": r"^HAI$",
            "KTHXBYE": r"^KTHXBYE$",
            "WAZZUP": r"^WAZZUP$",
            "BUHBYE": r"^BUHBYE$",
            "BTW": r"^BTW.*$",
            "OBTW": r"^OBTW.*$",
            "TLDR": r"^TLDR$",
            "I HAS A": r"^I HAS A (\w+)(?: ITZ (.+))?$",
            "VISIBLE": r"^VISIBLE (.+)$",
            "GIMMEH": r"^GIMMEH$",
            "O RLY?": r"^O RLY\?$",
            "YA RLY": r"^YA RLY$",
            "MEBBE": r"^MEBBE$",
            "NO WAI": r"^NO WAI$",
            "OIC": r"^OIC$",
            "WTF?": r"^WTF\?$",
            "OMG": r"^OMG$",
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
            "AN": r"^AN$"
        }

        # Continue with standard keyword matching
        for keyword, pattern in keywords.items():
            match = re.match(pattern, ' '.join(tokens))
            if match:
                if keyword == "I HAS A":
                    variable = match.group(1)
                    variable_value = match.group(2)
                    outputs = []
                    if variable_value:
                        self.variables[variable] = variable_value
                        tokens = self.tokenize(self.variables[variable])
                        for token in tokens:
                            outputs.append(f"Variable: {token}")
                        return f"Lexeme: {keyword}, Variable: {variable}, Lexeme: ITZ, {', '.join(outputs)}"
                    else:
                        self.variables[variable] = "NOOB"
                        return f"Lexeme: {keyword}, Variable: {variable}, Value: {self.variables[variable]}"

                if keyword == "VISIBLE":
                    value = match.group(1).strip()
                    outputs = []

                    tokens = self.tokenize(value)

                    for token in tokens:    
                        outputs.append(f"Variable: {token}")

                    return f"Lexeme: {keyword}, {', '.join(outputs)}"
                if keyword == "BTW":
                    return f"Lexeme: {keyword}, Comment: {' '.join(tokens[1:])}"

                return f"Lexeme: {keyword}"

        return None

    def extract(self, line):
        if line == "OBTW":
            self.comment_block = True
            return

        if self.comment_block:
            if line == "TLDR":
                self.comment_block = False
            return

        tokens = self.tokenize(line)
        parsed = self.parser(tokens)

        if parsed:
            print(parsed)

    def mainloop(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    self.extract(line)


root = tk.Tk()
app = Interpreter(root)
root.mainloop()