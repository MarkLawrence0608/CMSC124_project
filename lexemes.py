import re
import tkinter as tk
from tkinter import filedialog

class Lexemes:
    def __init__(self, keyword, value):
        self.keyword = keyword
        self.value = value

keywords = {
    r'^HAI$': 'Start of the program',
    r'^KTHXBYE$': 'End of the program',
    r'^WAZZUP$': 'Variable Declaration Block',
    r'^BUHBYE$': 'Variable Declaration End-Block',
    r'^BTW .*': 'Comment',
    r'^OBTW .*': 'Comment',
    r'^TLDR$': 'Comment End',
    r'^I HAS A [a-zA-Z][a-zA-Z0-9_]*$': 'Variable Declaration',
    r'^I HAS A [a-zA-Z][a-zA-Z0-9_]* ITZ .+$': 'Variable Declaration with Value',
    r'^ITZ$': 'Variable Assignment',
    r'^R .+$': 'Variable Assignment',
    r'^SUM OF .+$': 'Operation',
    r'^DIFF OF .+$': 'Operation',
    r'^PRODUKT OF .+$': 'Operation',
    r'^QUOSHUNT OF .+$': 'Operation',
    r'^MOD OF .+$': 'Operation',
    r'^BIGGR OF .+$': 'Operation',
    r'^SMALLR OF .+$': 'Operation',
    r'^BOTH OF .+$': 'Operation',
    r'^EITHER OF .+$': 'Operation',
    r'^WON OF .+$': 'Operation',
    r'^NOT .+$': 'Operation',
    r'^ANY OF .+$': 'Operation',
    r'^ALL OF .+$': 'Operation',
    r'^BOTH SAEM .+$': 'Operation',
    r'^DIFFRINT .+$': 'Operation',
    r'^SMOOSH .+$': 'Concatenation',
    r'^MAEK .+$': 'Typecasting',
    r"^A$": "Typecasting",
    r'^IS NOW A .+$': 'Typecasting',
    r'^VISIBLE .+$': 'Output',
    r'^GIMMEH .+$': 'Input',
    r'^O RLY\?$': 'Conditional',
    r'^YA RLY$': 'Conditional',
    r'^MEBBE .+$': 'Conditional',
    r'^NO WAI$': 'Conditional',
    r'^OIC$': 'Conditional',
    r'^WTF\?$': 'Conditional',
    r'^OMG .+$': 'Conditional',
    r'^IM IN YR .+$': 'Loop',
    r'^UPPIN .+$': 'Increment',
    r'^NERFIN .+$': 'Decrement',
    r'^YR .+$': 'Index',
    r'^TIL .+$': 'Loop',
    r'^WILE .+$': 'Loop',
    r'^IM OUTTA YR .+$': 'Loop-End',
    r'^HOW IZ I .+$': 'Function Declaration',
    r'^IF U SAY SO$': 'Function Return',
    r'^GTFO$': 'No Value Return',
    r'^FOUND YR .+$': 'Function Return',
    r'^I IZ .+$': 'Function Call',
    r'^MKAY$': 'Concatenation Delimiter',
    r'^NOOB$': 'Void Literal',
    r'^AN$': 'Separator',
}

class Lexer:
    def __init__(self, source_code):
        self.source_code = source_code.splitlines()
        self.tokens = []

    def tokenize(self):
        for line in self.source_code:
            line = line.strip()
            if line:
                matched = False
                for pattern, token_type in keywords.items():
                    if re.match(pattern, line):
                        self.tokens.append(Lexemes(token_type, line))
                        matched = True
                        break
                if not matched:
                    print("Lexeme unidentified")
                    break
        return self.tokens

def output_print(file_path):
    with open(file_path, 'r') as file:
        source_code = file.read()
    lexer = Lexer(source_code)
    tokens = lexer.tokenize()
    for token in tokens:
        print(f"{token.value}: {token.keyword}")

def open_file():
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename(title="Select a file")
    if file_path:
        output_print(file_path)

if __name__ == "__main__":
    open_file()
