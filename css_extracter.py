import requests as r
import sys
import re

if len(sys.argv <= 1):
    print("[Extraction Failed] 1 argument needed: the source HTML file .html")
    exit()
html_file = sys.argv[1]

assert html_file[-5:] == ".html"

try:
    with open(html_file, "r", encoding="UTF-8") as hf:
        html_doc = hf.read()
except:
    print("wrong file name")
    exit()


regex = re.compile("*\.css")
re.findall(regex, )
