from lxml import etree, html
from json import load as json_load
import sys
import util

def highlighter(html_file, json_file):

    # assert html_file[-5:].lower() == 'html', "HTML filename must ends with '.html'"
    # assert json_file[-5:].lower() == 'json', "JSON filename must ends with '.html'"

    # load HTML as ElementTree, load JSON as dictionary obj
    tree= html.parse(util.VIEW_DEFAULT + html_file)
    with open(json_file, "r") as f:
        json_data = json_load(f)

    # Mark the value data
    for value in json_data["pair"]:
        ele_val = tree.xpath(value["xpath"])
        ele_val[0].set("style", "background-color:skyblue")

    # Mark the attribute data
    attrib = value["attribute"]
    if attrib["xpath"] != "[None]":
        ele_attr = tree.xpath(attrib["xpath"])
        ele_attr[0].set("style", "background-color:magenta")

    tree.write_c14n(util.VIEW_DEFAULT+ html_file[:-5] + "_highlighted.html")

    # try:
    # except:
    #     print(sys.exc_info()[0]) # print error name
    #     print("Highlighter for '{}' Failed".format(html))




