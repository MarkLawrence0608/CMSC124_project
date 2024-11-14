import re
'''
Create Parser
Create Dictionary for RegEx
Identify SUM DIFF PRODUKT QUOSHUNT
SPACING
VARIABLES
'''
class Interpreter:
    # def __init__(self, root):
    #     self.root = root
    #     self.root.title("")
    #     self.create_widgets()
    
    def __init__(self, file_path):
        self.file_path = file_path
        self.variables = {}
        self.in_comment_block = False

    def run(self):
        with open(self.file_path, 'r') as file:
            for line in file:
                line = line.strip()

                if line == "OBTW":
                    self.in_comment_block = True
                    continue

                if self.in_comment_block:
                    if line == "TLDR":
                        self.in_comment_block = False
                    continue

                if "BTW" in line:
                    line = line.split("BTW", 1)[0].strip()

                token_pattern = r'"[^"]*"|\S+'
                tokens = re.findall(token_pattern, line)

                if not tokens:
                    continue

                if tokens[0] == "HAI":
                    continue

                elif tokens[0] == "KTHXBYE":
                    break

                elif tokens[0] == "I" and tokens[1] == "HAS" and tokens[2] == "A":
                    var_name = tokens[3]
                    self.variables[var_name] = None
                    print(f"Variable: ", var_name)

                elif tokens[0] == "VISIBLE":
                    expr = ' '.join(tokens[1:])
                    if expr.startswith('"') and expr.endswith('"'):
                        print(expr)
                    elif expr in self.variables:
                        print(self.variables[expr])

interpreter = Interpreter("01_variables.lol")
interpreter.run()
