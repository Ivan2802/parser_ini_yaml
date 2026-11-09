class Serializer:
    def __init__(self, tree):
        self.tree = tree

    def serialize(self):
        tree = self.tree
        with open("yaml.yaml", "w", encoding="utf-8") as file:
            for com in tree.comments:
                file.write("# " + com.value.value)
            for g_entry in tree.entries:
                for e in g_entry:
                    file.write(e.key.value + ": " + e.value.value)
                    file.write("\n")
            for section_i in range(len(tree.sections)):
                section = tree.sections[section_i]
                if section_i != 0:
                    file.write("\n")
                file.write(section.name + ": ")
                file.write("\n")
                for entry in section.entries:
                    if "," in entry.value.value:
                        items_list = entry.value.value.split(",")
                        file.write("  " + entry.key.value + ":")
                        file.write("\n")
                        for item in items_list:
                            file.write("    -" + item)
                            file.write("\n")
                    else:
                        file.write("  " + entry.key.value + ":" + entry.value.value)
                        file.write("\n")