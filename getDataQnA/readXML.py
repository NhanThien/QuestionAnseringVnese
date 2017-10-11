import xml.etree.ElementTree as ET
from xml.dom import minidom

tree = ET.parse('Datatoken/a12.xml')
root = tree.getroot()
print root
# xmldoc = minidom.parse('Datatoken/a12.xml')
# itemlist = xmldoc.getElementsByTagName('w')
# print(len(itemlist))
# print(itemlist[0].attributes['pos'].value)
# for s in itemlist:
#     print(s.attributes['pos'].value)