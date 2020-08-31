from lxml import etree


parser = etree.XMLParser(recover=True)
tree = etree.parse('reddit.xml', parser=parser)

i = 0
for index, element in enumerate(tree.getiterator('utt')):
    print(element.text)
    i += 1

    if i > 10:
        break
