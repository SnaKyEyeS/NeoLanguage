from tqdm import tqdm
from lxml import etree


parser = etree.XMLParser(recover=True)
tree = etree.parse('reddit.xml', parser=parser)
print(len(tree.xpath('//utt')))

for el in tqdm(tree.xpath('//utt')):
    pass
