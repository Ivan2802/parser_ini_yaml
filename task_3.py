import configparser
import xml.etree.ElementTree as ET

config = configparser.ConfigParser()
config.read("ini.ini", encoding="utf-8")

root = ET.Element("ini")

for section in config.sections():
    section_elem = ET.SubElement(root, "section")
    section_elem.set("name", section)
    
    for key, value in config[section].items():
        entry = ET.SubElement(section_elem, "entry")
        key_elem = ET.SubElement(entry, "key")
        key_elem.text = key
        val_elem = ET.SubElement(entry, "value")
        val_elem.text = value

ET.indent(root, space="  ", level=0)
tree = ET.ElementTree(root)
tree.write("file.xml", encoding="utf-8", xml_declaration=True)
