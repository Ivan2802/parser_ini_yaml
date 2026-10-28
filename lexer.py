class Lexer:
    def __init__(self, text):
        self.text = text
        self.tokens = list()

    token_dict = {"LB": "[", "RB": "]", "VALUE": "", "EQ": "=", "KEY": ""}
    # add comments

    def tokenizate(self):
        lines = self.text
        for i in range(len(lines)):
            line = lines[i]
            # line = line.replace(" ", "")
            if line[0] == self.token_dict["LB"]:
                line = line.replace(" ", "")
                t_lb = Token("LB", self.token_dict["LB"])
                t_val = Token("VALUE", line[1:-2])
                t_rb = Token("RB", self.token_dict["RB"])
                self.tokens.extend([t_lb, t_val, t_rb])
            elif line[0] == '\n':
                t_nl = Token("NL", "\n")
                self.tokens.append(t_nl)
            else:
                line = line.split(self.token_dict["EQ"])
                t_k = Token("KEY", line[0].replace(" ", ""))
                t_eq = Token("EQ", self.token_dict["EQ"])
                t_v = Token("VALUE", line[-1].rstrip())
                self.tokens.extend([t_k, t_eq, t_v])
        return self.tokens


class Token:
    def __init__(self, type, value):
        self.type = type
        self.value = value