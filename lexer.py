class Lexer:
    def __init__(self, text):
        self.pos = 0
        self.text = text
        self.tokens = list()