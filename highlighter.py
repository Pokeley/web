from bs4 import BeautifulSoup
from lxml import etree, html
import json
import sys

# filename : sys.argv[1]


if len(sys.argv) > 1 and sys.argv[1] == "--help":
    print("Usage: python highlighter.py [HTML file] [JSON file]")

try:
    html_file = sys.argv[1]
    json_file = sys.argv[2]

    tree= html.parse('./' + html_file)

    #f = open(html_file, "r")
    #html_doc = f.read()
    #f.close()
    with open(json_file, "r") as f:
        json_data = json.load(f)


except IndexError:
    print("To check usage, type 'python highliter.py --help")
    exit()
except FileNotFoundError as e:
    print(e)
    print("To check usage, type 'python highliter.py --help")
    exit()


# soup = BeautifulSoup(html_doc, 'html.parser')
# tree = html.fromstring(html_doc)

for value in json_data["pair"]:
    ele_val = tree.xpath(value["xpath"])
    ele_val[0].set("style", "background-color:skyblue")

    attrib = value["attribute"]
    if attrib["xpath"] != "[None]":
        ele_attr = tree.xpath(attrib["xpath"])
        ele_attr[0].set("style", "background-color:magenta")

tree.write_c14n(html_file[:-5] + "_highlighted.html")

# ele = tree.xpath("//*[@id=\"tab-panel-0-w3\"]/div[1]/span/h2")

