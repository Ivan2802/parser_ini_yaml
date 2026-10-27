import lexer

def main():
    with open("ini.txt", "r", encoding="utf-8") as file:
        lines = file.readlines()
        text = "".join(lines)

if __name__ == "__main__":
    main()