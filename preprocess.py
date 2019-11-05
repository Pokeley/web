import requests as r
import sys
import re


def css_extracter(html_file):
    # assert html_file[-5:].lower() == ".html", "HTML filename must ends with '.html'"


    with open(html_file, "r", encoding="UTF-8") as hf:
        html_doc = hf.read()

    # TODO: improve algorithm with lxml ElementTree
    regex = re.compile("(http.:\/|\.)(\/[^<>\s]*)*\.css", re.IGNORECASE)
    css_list = re.findall(regex, html_doc)


    # try:
    # except:
    #     print("[ERROR] css_extracter(html_file) in preprocessor.py")
    #     print("Wrong file name:", html_file)


