import lexer
import parser
import serializer

def main():
    with open("ini.ini", "r", encoding="utf-8") as file:
        text = file.readlines()
        tokens = lexer.Lexer(text).tokenizate()
        as_tree = parser.Parser(tokens).parse_ini()
        translator = serializer.Serializer(as_tree)
        translator.serialize()

if __name__ == "__main__":
    main()