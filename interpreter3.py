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
        self.lines = []
        self.gui_widgets()

    def gui_widgets(self):
        self.canvas = tk.Canvas(self.root, width=300, height=300, bg='white', borderwidth=0, highlightthickness=0, relief=tk.SOLID)
        self.canvas.pack(side=tk.TOP, padx=(2, 0), pady=(2, 0))
        self.mainloop()

    def tokenize(self, line):
        token_pattern = r'"[^"]*"|\S+|[.]'  
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
            "OBTW": r"^OBTW$",
            "TLDR": r"^TLDR$",
            "I HAS A": r"^I HAS A (\w+)(?: ITZ (.+))?$",
            "VISIBLE": r"^VISIBLE (.+)$",
            "GIMMEH": r"^GIMMEH (.+)$",
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
            "AN": r"^AN$",
            "BOTH SAEM": r"^BOTH SAEM (\w+)(?: AN (.+))?$"
        }

        for keyword, pattern in keywords.items():
            match = re.match(pattern, ' '.join(tokens))
            if match:
                if keyword == "I HAS A":
                    variable = match.group(1)
                    variable_value = match.group(2)
                    
                    variable_pattern = r'^[A-Za-z]+[0-9A-Za-z_]*$'
                    numbr = r'^-?[0-9]+$' 
                    numbar = r'^-?[0-9]+\.[0-9]+$'
                    yarn =  r'^".*"$'
                    troof = r'^(WIN|FAIL)$'  
                    complex_patterns = r'^(SUM OF .*|DIFF OF .*|PRODUKT OF .*|QUOSHUNT OF .*)$'
                    
                    if not re.match(variable_pattern, variable):
                            return f"Error: Invalid variable '{variable}'."
 
                    if variable_value == None:
                        return
                    
                    if not re.match(complex_patterns, variable_value) and not re.match(numbr, variable_value) and not re.match(numbar, variable_value) and not re.match(yarn, variable_value) and not re.match(troof, variable_value):
                            return f"Error: Invalid literal '{variable_value}'."
                    


                    if variable_value:
                        self.variables[variable] = variable_value
                        return f"Variable '{variable}' is assigned: {self.variables[variable]}"
                    else:
                        self.variables[variable] = "NOOB"
                        return f"Variable '{variable}' is assigned default value: {self.variables[variable]}"

                if keyword == "GIMMEH":
                    variable = match.group(1).strip()
                    
                    variable_pattern = r'^[A-Za-z]+[0-9A-Za-z_]*$' 
                    
                    if not re.match(variable_pattern, variable):
                            return f"Error: Invalid variable '{variable}'."
            
                    return f"User Input is assigned to: '{variable}' "

                if keyword == "VISIBLE":
                    value = match.group(1).strip()
                    return f"Output: {value}"

                if keyword == "BTW":
                    return f"Comment: {' '.join(tokens[1:])}"
                
                if keyword == "HAI":
                    return f"Start of program: {keyword}"
                
                if keyword == "KTHXBYE":
                    return f"End of program: {keyword}"
                
                if keyword == "BUHBYE":
                    return f"End of variable section: {keyword}"
                
                if keyword == "WAZZUP":
                    return f"Start of variable section: {keyword}"
    
                if keyword == "O RLY?":
                    return f"Conditional declaration: {keyword}"
                    
                
                if keyword == "YA RLY?":
                    return f"conditional IF: {keyword}"
                    
                
                if keyword == "NO WAI":
                    return f"Conditional ELSE: {keyword}"
                    
                
                if keyword == "MEBBE":
                    return f"Conditional ELSE-IF: {keyword}, Condition: {' '.join(tokens[1:])}"
                
                if keyword == "OIC":
                    return f"End of Conditonal declaration: {keyword}"
                
                if keyword == "BOTH SAEM":
                    compare1 = match.group(1)
                    compare2 = match.group(2)
                    
                    variable_pattern = r'^([A-Za-z]+[0-9A-Za-z_]*)|[0-9]+$' 
                    
                    if not re.match(variable_pattern, compare1):
                            return f"Error: Invalid variable or literal '{variable}'."
                    if not re.match(variable_pattern, compare2):
                            return f"Error: Invalid variable or literal '{variable}'."
            
                    return f"Comparison: '{compare1}' == '{compare2}' "


                return f"Lexeme: {keyword}"

        return f"Syntax Error: Unrecognized statement or incorrect syntax."

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
            return parsed  
        
        

    def mainloop(self):
        file = open(self.file_path, 'r') 
        for line in file:
                line = line.strip()
                self.lines.append(line)

        first_non_comment_line = None
        for line in self.lines:
            if line and not line.startswith(('OBTW', 'BTW', 'TLDR')):
                first_non_comment_line = line
                break

        if not first_non_comment_line or first_non_comment_line != "HAI":
            print("Error: Program must start with 'HAI', a function, or a comment.")
            return  

        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()
                if line:
                    error = self.extract(line)
                if error and "Syntax Error" in error:
                    break  

        if self.lines and self.lines[-1] != "KTHXBYE":
            print("Error: Program must end with 'KTHXBYE'.")
            return  

    # def syntax_analyzer(self, line):
    #     tokens = self.tokenize(line)

    #     keywords = {
    #     "HAI": r"^HAI$",
    #     "KTHXBYE": r"^KTHXBYE$",
    #     "WAZZUP": r"^WAZZUP$",
    #     "BUHBYE": r"^BUHBYE$",
    #     "BTW": r"^BTW.*$",
    #     "OBTW": r"^OBTW$",
    #     "TLDR": r"^TLDR$",
    #     "I HAS A": r"^I HAS A (\w+)(?: ITZ (.+))?$",
    #     "VISIBLE": r"^VISIBLE (.+)$",
    #     "GIMMEH": r"^GIMMEH$",
    #     "O RLY?": r"^O RLY\?$",
    #     "YA RLY": r"^YA RLY$",
    #     "MEBBE": r"^MEBBE$",
    #     "NO WAI": r"^NO WAI$",
    #     "OIC": r"^OIC$",
    #     "WTF?": r"^WTF\?$",
    #     "OMG": r"^OMG$",
    #     "IM IN YR": r"^IM IN YR$",
    #     "UPPIN": r"^UPPIN$",
    #     "NERFIN": r"^NERFIN$",
    #     "YR": r"^YR$",
    #     "TIL": r"^TIL$",
    #     "WILE": r"^WILE$",
    #     "IM OUTTA YR": r"^IM OUTTA YR$",
    #     "HOW IZ I": r"^HOW IZ I$",
    #     "IF U SAY SO": r"^IF U SAY SO$",
    #     "GTFO": r"^GTFO$",
    #     "FOUND YR": r"^FOUND YR$",
    #     "I IZ": r"^I IZ$",
    #     "MKAY": r"^MKAY$",
    #     "AN": r"^AN$"
    #     }


        

root = tk.Tk()
app = Interpreter(root)
root.mainloop()
