
from lxml import etree
html = etree.parse("book.html")
result = html.xpath("/bookstore")
print(len(result))
