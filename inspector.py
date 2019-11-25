from lxml import etree, html
from json import load as json_load
import sys
import util

def highlighter(json_file):

    # assert html_file[-5:].lower() == 'html', "HTML filename must ends with '.html'"
    # assert json_file[-5:].lower() == 'json', "JSON filename must ends with '.html'"

    # load HTML as ElementTree, load JSON as dictionary obj
    
    with open(json_file, "r") as f:
        json_data = json_load(f)

    # Mark the value data
    for site in json_data:
        html_file = site["node"] + ".html"
        tree= html.parse(util.VIEW_DEFAULT + html_file)
        
        for data in site["element_attrs"].keys():
	        ele_val = tree.xpath(data["value_xpath"])
	        ele_val[0].set("style", "background-color:skyblue")

		    # Mark the attribute data
		    
		    if data["attr_xpath"] != "[NONE]":
		        ele_attr = tree.xpath(data["attr_xpath"])
		        ele_attr[0].set("style", "background-color:magenta")

	    tree.write_c14n(util.VIEW_DEFAULT+ "highlited/" + html_file[:-5] + "_hl.html")

    # try:
    # except:
    #     print(sys.exc_info()[0]) # print error name
    #     print("Highlighter for '{}' Failed".format(html))




