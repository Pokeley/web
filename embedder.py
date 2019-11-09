from lxml import etree, html
from os.path import isfile
from os import getcwd
import sys
import util

class Embedder:

    def __init__(self, html_filename, clean=True):
        self.filename = html_filename
        self.DomTree = html.parse(util.VIEW_DEFAULT + html_filename)
        if clean: self._clean_nodes()
        self._assign_id()
        self.features = self._visual_embedding()


    def iter(self, onlyElement=True):
        if onlyElement:
            return self.DomTree.getiterator(tag=etree.Element)
        return self.DomTree.getiterator()

    def find_node(self, node_id):
        for node in self.iter():
            if node.attrib["node_id"] == node_id:
                return node
        return None

    def print_processed_tree(self):
        self.Domtree.write_c14n( \
            util.VIEW_DEFAULT + html_file[:-5] + "_processed.html")

    def __new__(cls, filename, clean=True):
        if isfile(util.VIEW_DEFAULT + filename):
            return super(Embedder, cls).__new__(cls)
        else:
            print("[Embedder Error] Cannot find html file on given path '{}'... Embedder not generated"\
                .format(getcwd() + "\\\\" + util.VIEW_DEFAULT[:-1] + "\\\\" + filename))
            return None

    def _clean_nodes(self):
        cnt = 0
        dirty = True
        while dirty:
            dirty = False
            for node in self.iter(onlyElement=False):
                if type(node) == html.HtmlComment:
                    parent = node.getparent()
                    # print("WOWWWWWW COMMENT Before:", parent.getchildren())
                    
                    parent.remove(node)   # Remove that node!
                    # print("After:", parent.getchildren())
                    
                    continue
                if not node.getchildren() and not node.text:
                    parent = node.getparent()
                    # print("Before:", parent.getchildren())
                    
                    parent.remove(node)   # Remove that node!
                    # print("After:", parent.getchildren())
                    dirty = True

    def num_of_nodes(self, onlyElement=False):
        count = 0
        for a in self.iter(onlyElement):
            print(a)
            count += 1
        return count





        # if not cleaned:
        #     cleaning $u$
        #     return _clean_nodes
        # if cleaned:
        #     return 0
        pass

    def _assign_id(self):
        id_inc = -1
        for node in self.iter():
            if (type(node) == html.HtmlComment):
                continue
            id_inc += 1
            node_id = hex(id_inc)[2:]    #[2:] : to exclude '0x'
            # hex(int): return hexadecimal format of the num as string type

            node.set(util.PREFIX+"_id", node_id)

    def _visual_embedding(self):
        pass




