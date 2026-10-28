class Parser:
    def __init__(self, tokens, pos=0):
        self.tokens = tokens
        self.pos = pos
    
    def parse_ini(self):
        section_list = list()
        entries_list = list()
        while self.pos < len(self.tokens):
            if self.tokens[self.pos].type == "LB":
                section_list.append(self.parse_section())
            elif self.tokens[self.pos].type == "KEY":
                entries_list.append(self.parse_entries())
            elif self.tokens[self.pos].type == "NL":
                self.expect("NL")
        return Ini(entries_list, section_list)
    
    def parse_section(self):
        self.expect("LB")
        name = self.expect("VALUE").value
        self.expect("RB")
        entries = self.parse_entries()
        return Section(name, entries)

    def parse_entries(self):
        entries_list = list()
        while self.pos < len(self.tokens) and self.tokens[self.pos].type == "KEY":
            key = self.expect("KEY")
            self.expect("EQ")
            value = self.expect("VALUE")
            entries_list.append(Entry(key, value))
        return entries_list
    


    def expect(self, type):
        t = self.tokens[self.pos]
        if t.type != type:
            return "ParserError" # лучше выбрасывать ошибку raise
        self.pos += 1
        return t
    
class Ini:
    def __init__(self, entries, sections):
        self.entries = entries
        self.sections = sections

class Section:
    def __init__(self, name, entries):
        self.name = name
        self.entries = entries

class Entry:
    def  __init__(self, key, value):
        self.key = key
        self.value = value