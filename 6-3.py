#读取xml
from xml.etree.cElementTree import parse
f=open('a.xml')
et=parse(f)
root=et.getroot()
for child in root:
    for subchild in child:
        print(subchild)


