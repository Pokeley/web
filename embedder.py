from lxml import etree, html
from os.path import isfile
from os import getcwd
import sys
import util


class Embedder:
    def __new__(cls, filename):
        if isfile(util.VIEW_DEFAULT + filename):
            return super(Embedder, cls).__new__(cls)
        else:
            print("[Embedder Error] Cannot find html file on given path '{}'... Embedder not generated"\
                .format(getcwd() + "\\\\" + util.VIEW_DEFAULT[:-1] + "\\\\" + filename))
            return None

    def __init__(self, html_filename):
        self.filename = html_filename
        self.DomTree = html.parse(util.VIEW_DEFAULT + html_filename)
        self._assign_id()

    def _assign_id(self):
        id_inc = -1
        for node in self.iter():
            if (type(node) == html.HtmlComment):
                continue
            id_inc += 1
            node_id = hex(id_inc)[2:]    #[2:] : to exclude '0x'
            # hex(int): return hexadecimal format of the num as string type

            node.set(util.PREFIX+"_id", node_id)

    def iter(self, onlyElement=True):
        if onlyElement:
            return self.DomTree.getiterator(tag=etree.Element)
        return self.DomTree.getiterator()


    def find_node(self, node_id):
        for node in self.iter():
            if node.attrib["node_id"] == node_id:
                return node
        return None



if False:
    if len(sys.argv) <= 1:
        print("[Extraction Failed] 1 argument needed: the source HTML file '*.html'")
        exit()

    html_file = sys.argv[1]
    assert html_file[-5:].lower() == ".html", "HTML filename must ends with '.html'"

    # with html.parse('./' + html_file) as tree:
    #     print("You get in!")

    # print("Still there?")


    try:
        tree= html.parse('./' + html_file)

        node_iterator = tree.getiterator()
        all_nodes = list(node_iterator)

        id_inc = -1
        for node in all_nodes:
            if (type(node) == html.HtmlComment):
                continue

            id_inc += 1
            node_id = hex(id_inc)[2:]    #[2:] : to exclude '0x'
            # hex(int): return hexadecimal format of the num as string type
            node.set("node_id", node_id)

        #tree.write_c14n(html_file[:-5] + "_embedded.html")


    except IndexError:
        print("To check usage, type 'python highliter.py --help")
    except FileNotFoundError as e:
        print(e)
        print("To check usage, type 'python highliter.py --help")
    except OSError as e:
        print(e)
        print("To check usage, type 'python highliter.py --help")


